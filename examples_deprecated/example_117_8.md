# Description
Combining statements with family-level support using is_a or part_of relationships.

# Code
```
import os
import unittest
from indra.preassembler import Preassembler
from indra.statements import *

def test_superfamily_refinement_isa_or_partof():
    src = Agent('SRC', db_refs={'HGNC': '11283'})
    prkag1 = Agent('PRKAG1', db_refs={'HGNC': '9385'})
    ampk = Agent('AMPK', db_refs={'FPLX': 'AMPK'})
    st1 = Phosphorylation(src, ampk, 'tyrosine', '32')
    st2 = Phosphorylation(src, prkag1, 'tyrosine', '32')
    pa = Preassembler(bio_ontology, stmts=[st1, st2])
    stmts = pa.combine_related()
    # The top-level list should contain only one statement, the gene-level
    # one, supported by the family one.
    assert len(stmts) == 1
    assert stmts[0].equals(st2)
    assert len(stmts[0].supported_by) == 1

```
