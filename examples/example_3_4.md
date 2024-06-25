# Description
Inference of Modification from RegulateActivity and ActiveForm Statements

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

    def infer_modifications(stmts):
        """Return inferred Modification from RegulateActivity + ActiveForm.

        This function looks for combinations of Activation/Inhibition Statements
        and ActiveForm Statements that imply a Modification Statement.
        For example, if we know that A activates B, and phosphorylated B is
        active, then we can infer that A leads to the phosphorylation of B.
        An additional requirement when making this assumption is that the
        activity of B should only be dependent on the modified state and not
        other context - otherwise the inferred Modification is not necessarily
        warranted.

        Parameters
        ----------
        stmts : list[indra.statements.Statement]
            A list of Statements to infer Modifications from.

        Returns
        -------
        linked_stmts : list[indra.mechlinker.LinkedStatement]
            A list of LinkedStatements representing the inferred Statements.
        """
        linked_stmts = []
        for act_stmt in _get_statements_by_type(stmts, RegulateActivity):
            for af_stmt in _get_statements_by_type(stmts, ActiveForm):
                if not af_stmt.agent.entity_matches(act_stmt.obj):
                    continue
                mods = af_stmt.agent.mods
                # Make sure the ActiveForm only involves modified sites
                if af_stmt.agent.mutations or \
                    af_stmt.agent.bound_conditions or \
                    af_stmt.agent.location:
                    continue
                if not af_stmt.agent.mods:
                    continue
                for mod in af_stmt.agent.mods:
                    evs = act_stmt.evidence + af_stmt.evidence
                    for ev in evs:
                        ev.epistemics['direct'] = False
                    if mod.is_modified:
                        mod_type_name = mod.mod_type
                    else:
                        mod_type_name = modtype_to_inverse[mod.mod_type]
                    mod_class = modtype_to_modclass[mod_type_name]
                    if not mod_class:
                        continue
                    st = mod_class(act_stmt.subj,
                                   act_stmt.obj,
                                   mod.residue, mod.position,
                                   evidence=evs)
                    ls = LinkedStatement([act_stmt, af_stmt], st)
                    linked_stmts.append(ls)
                    logger.info('inferred: %s' % st)

```
