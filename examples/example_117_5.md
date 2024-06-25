# Description
Combining statements with exact duplicate evidence.

# Code
```
import os
import unittest
from indra.preassembler import Preassembler
from indra.statements import *

def test_combine_evidence_exact_duplicates():
    raf = Agent('RAF1')
    mek = Agent('MEK1')
    p1 = Phosphorylation(raf, mek,
            evidence=Evidence(text='foo'))
    p2 = Phosphorylation(raf, mek,
            evidence=Evidence(text='bar'))
    p3 = Phosphorylation(raf, mek,
            evidence=Evidence(text='bar'))
    stmts = [p1, p2, p3]
    pa = Preassembler(bio_ontology, stmts=stmts)
    pa.combine_duplicates()
    # The statements come out sorted by their matches_key
    assert len(pa.unique_stmts) == 1
    assert len(pa.unique_stmts[0].evidence) == 2
    assert set(ev.text for ev in pa.unique_stmts[0].evidence) == \

```
