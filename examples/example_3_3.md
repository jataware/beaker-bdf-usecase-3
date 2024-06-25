# Description
Inference of ActiveForm from RegulateActivity and Modification Statements

# Code
```
import uuid
import logging
import networkx
import itertools
from indra.util import fast_deepcopy
from indra.statements import *
from indra.ontology.bio import bio_ontology

def _get_statements_by_type(stmts, stmt_type):
    return [st for st in stmts if isinstance(st, stmt_type)]

logger = logging.getLogger(__name__)

class LinkedStatement(object):
    def __init__(self, source_stmts, inferred_stmt):
        self.source_stmts = source_stmts
        self.inferred_stmt = inferred_stmt

class ActiveForm(Statement):
    pass

class Modification(Statement):
    pass

class RegulateActivity(Statement):
    pass

class Agent(object):
    def __init__(self, name, mods=None, db_refs=None):
        self.name = name
        self.mods = mods

    def infer_active_forms(stmts):
        """Return inferred ActiveForm from RegulateActivity + Modification.

        This function looks for combinations of Activation/Inhibition
        Statements and Modification Statements, and infers an ActiveForm
        from them. For example, if we know that A activates B and
        A phosphorylates B, then we can infer that the phosphorylated form
        of B is active.

        Parameters
        ----------
        stmts : list[indra.statements.Statement]
            A list of Statements to infer ActiveForms from.

        Returns
        -------
        linked_stmts : list[indra.mechlinker.LinkedStatement]
            A list of LinkedStatements representing the inferred Statements.
        """
        linked_stmts = []
        for act_stmt in _get_statements_by_type(stmts, RegulateActivity):
            # TODO: revise the conditions here
            if not (act_stmt.subj.activity is not None and
                act_stmt.subj.activity.activity_type == 'kinase' and
                act_stmt.subj.activity.is_active):
                continue
            matching = []
            ev = act_stmt.evidence
            for mod_stmt in _get_statements_by_type(stmts, Modification):
                if mod_stmt.enz is not None:
                    if mod_stmt.enz.entity_matches(act_stmt.subj) and \
                        mod_stmt.sub.entity_matches(act_stmt.obj):
                        matching.append(mod_stmt)
                        ev.extend(mod_stmt.evidence)
            if not matching:
                continue
            mods = []
            for mod_stmt in matching:
                mod_type_name = mod_stmt.__class__.__name__.lower()
                if isinstance(mod_stmt, AddModification):
                    is_modified = True
                else:
                    is_modified = False
                    mod_type_name = mod_type_name[2:]
                mc = ModCondition(mod_type_name, mod_stmt.residue,
                                  mod_stmt.position, is_modified)
                mods.append(mc)
            source_stmts = [act_stmt] + [m for m in matching]
            st = ActiveForm(Agent(act_stmt.obj.name, mods=mods,
                                  db_refs=act_stmt.obj.db_refs),
                            act_stmt.obj_activity, act_stmt.is_activation,
                            evidence=ev)
            linked_stmts.append(LinkedStatement(source_stmts, st))
            logger.info('inferred: %s' % st)

```
