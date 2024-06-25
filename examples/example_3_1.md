# Description
Inference of Complexes from Statements implying physical interaction

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

class Complex(Statement):

    def infer_complexes(stmts):
        """Return inferred Complex from Statements implying physical interaction.

        Parameters
        ----------
        stmts : list[indra.statements.Statement]
            A list of Statements to infer Complexes from.

        Returns
        -------
        linked_stmts : list[indra.mechlinker.LinkedStatement]
            A list of LinkedStatements representing the inferred Statements.
        """
        interact_stmts = _get_statements_by_type(stmts, Modification)
        linked_stmts = []
        for mstmt in interact_stmts:
            if mstmt.enz is None:
                continue
            st = Complex([mstmt.enz, mstmt.sub], evidence=mstmt.evidence)
            linked_stmts.append(st)

```
