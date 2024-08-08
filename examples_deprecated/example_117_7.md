# Description
Combining related gene-level statements supported by family-level statements.

# Code
```
import os
import unittest
from indra.preassembler import Preassembler
from indra.statements import *

def test_superfamily_refinement():
    """A gene-level statement should be supported by a family-level
    statement."""
    src = Agent('SRC', db_refs={'HGNC': '11283'})
    ras = Agent('RAS', db_refs={'FPLX': 'RAS'})
    nras = Agent('NRAS', db_refs={'HGNC': '7989'})
    st1 = Phosphorylation(src, ras, 'tyrosine', '32')
    st2 = Phosphorylation(src, nras, 'tyrosine', '32')
    pa = Preassembler(bio_ontology, stmts=[st1, st2])
    stmts = pa.combine_related()
    # The top-level list should contain only one statement, the gene-level
    # one, supported by the family one.
    assert len(stmts) == 1, stmts
    assert (stmts[0].equals(st2))
    assert (len(stmts[0].supported_by) == 1)

```
