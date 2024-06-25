# Description
Combining statements with slightly different raw text for agents.

# Code
```
import os
import unittest
from indra.preassembler import Preassembler
from indra.statements import *

def test_combine_evidence_exact_duplicates_different_raw_text():
    raf1 = Agent('RAF1', db_refs={'TEXT': 'Raf'})
    raf2 = Agent('RAF1', db_refs={'TEXT': 'RAF'})
    mek = Agent('MEK1')
    p1 = Phosphorylation(raf1, mek,
            evidence=Evidence(text='foo'))
    p2 = Phosphorylation(raf1, mek,
            evidence=Evidence(text='bar'))
    p3 = Phosphorylation(raf2, mek,
            evidence=Evidence(text='bar'))
    stmts = [p1, p2, p3]
    pa = Preassembler(bio_ontology, stmts=stmts)
    pa.combine_duplicates()
    # The statements come out sorted by their matches_key
    assert len(pa.unique_stmts) == 1
    assert len(pa.unique_stmts[0].evidence) == 3
    assert set(ev.text for ev in pa.unique_stmts[0].evidence) == \

```
