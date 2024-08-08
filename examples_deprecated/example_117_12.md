# Description
Combining statements with bound conditions more specific than others.

# Code
```
import os
import unittest
from indra.preassembler import Preassembler
from indra.statements import *

def test_bound_condition_refinement():
    """A statement with more specific bound context should be supported by a
    less specific statement."""
    src = Agent('SRC', db_refs={'HGNC': '11283'})
    gtp = Agent('GTP', db_refs={'CHEBI': '15996'})
    nras = Agent('NRAS', db_refs={'HGNC': '7989'})
    nrasgtp = Agent('NRAS', db_refs={'HGNC': '7989'},
        bound_conditions=[BoundCondition(gtp, True)])
    st1 = Phosphorylation(src, nras, 'tyrosine', '32')
    st2 = Phosphorylation(src, nrasgtp, 'tyrosine', '32')
    # The top-level list should contain only one statement, the more specific
    # modification, supported by the less-specific modification.
    pa = Preassembler(bio_ontology, stmts=[st1, st2])
    stmts = pa.combine_related()
    assert len(stmts) == 1
    assert stmts[0].equals(st2)
    assert len(stmts[0].supported_by) == 1

```
