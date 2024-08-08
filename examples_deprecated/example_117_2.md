# Description
Combining duplicate statements and keeping original evidence using Preassembler.

# Code
```
import os
import unittest
from indra.preassembler import Preassembler
from indra.statements import *

def test_duplicates_copy():
    src = Agent('SRC', db_refs={'HGNC': '11283'})
    ras = Agent('RAS', db_refs={'FA': '03663'})
    st1 = Phosphorylation(src, ras, evidence=[Evidence(text='Text 1')])
    st2 = Phosphorylation(src, ras, evidence=[Evidence(text='Text 2')])
    stmts = [st1, st2]
    pa = Preassembler(bio_ontology, stmts=stmts)
    pa.combine_duplicates()
    assert len(pa.unique_stmts) == 1
    assert len(stmts) == 2
    assert len(stmts[0].evidence) == 1

```
