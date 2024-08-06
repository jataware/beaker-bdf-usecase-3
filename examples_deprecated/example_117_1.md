# Description
An example of combining duplicate statements using INDRA's Preassembler.

# Code
```
import os
import unittest
from indra.preassembler import Preassembler
from indra.statements import *

def test_duplicates():
    src = Agent('SRC', db_refs={'HGNC': '11283'})
    ras = Agent('RAS', db_refs={'FA': '03663'})
    st1 = Phosphorylation(src, ras)
    st2 = Phosphorylation(src, ras)
    pa = Preassembler(bio_ontology, stmts=[st1, st2])
    pa.combine_duplicates()

```
