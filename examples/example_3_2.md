# Description
Inference of RegulateActivity from Modification and ActiveForm Statements

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

class Activation(Statement):
    pass

class Inhibition(Statement):
    pass

class ActiveForm(Statement):
    pass

class Modification(Statement):

    def infer_activations(stmts):
        """Return inferred RegulateActivity from Modification + ActiveForm.

        This function looks for combinations of Modification and ActiveForm
        Statements and infers Activation/Inhibition Statements from them.
        For example, if we know that A phosphorylates B, and the
        phosphorylated form of B is active, then we can infer that
        A activates B. This can also be viewed as having "explained" a given
        Activation/Inhibition Statement with a combination of more mechanistic
        Modification + ActiveForm Statements.

        Parameters
        ----------
        stmts : list[indra.statements.Statement]
            A list of Statements to infer RegulateActivity from.

        Returns
        -------
        linked_stmts : list[indra.mechlinker.LinkedStatement]
            A list of LinkedStatements representing the inferred Statements.
        """
        linked_stmts = []
        af_stmts = _get_statements_by_type(stmts, ActiveForm)
        mod_stmts = _get_statements_by_type(stmts, Modification)
        for af_stmt, mod_stmt in itertools.product(*(af_stmts, mod_stmts)):
            # There has to be an enzyme and the substrate and the
            # agent of the active form have to match
            if mod_stmt.enz is None or \
                (not af_stmt.agent.entity_matches(mod_stmt.sub)):
                continue
            # We now check the modifications to make sure they are consistent
            if not af_stmt.agent.mods:
                continue
            found = False
            for mc in af_stmt.agent.mods:
                if mc.mod_type == modclass_to_modtype[mod_stmt.__class__] and \
                    mc.residue == mod_stmt.residue and \
                    mc.position == mod_stmt.position:
                    found = True
            if not found:
                continue
            # Collect evidence
            ev = mod_stmt.evidence
            # Finally, check the polarity of the ActiveForm
            if af_stmt.is_active:
                st = Activation(mod_stmt.enz, mod_stmt.sub, af_stmt.activity,
                                evidence=ev)
            else:
                st = Inhibition(mod_stmt.enz, mod_stmt.sub, af_stmt.activity,
                                evidence=ev)
            linked_stmts.append(LinkedStatement([af_stmt, mod_stmt], st))

```
