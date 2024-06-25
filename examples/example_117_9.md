# Description
Combining statements with more specific modifications supported by general modifications.

# Code
```
import os
import unittest
from indra.preassembler import Preassembler
from indra.statements import *

def test_modification_refinement():
    """A more specific modification statement should be supported by a more
    generic modification statement."""
    src = Agent('SRC', db_refs={'HGNC': '11283'})
    nras = Agent('NRAS', db_refs={'HGNC': '7989'})
    st1 = Phosphorylation(src, nras, 'tyrosine', '32')
    st2 = Phosphorylation(src, nras)
    pa = Preassembler(bio_ontology, stmts=[st1, st2])
    stmts = pa.combine_related()
    # The top-level list should contain only one statement, the more specific
    # modification, supported by the less-specific modification.
    assert len(stmts) == 1
    assert stmts[0].equals(st1)
    assert len(stmts[0].supported_by) == 1

```
