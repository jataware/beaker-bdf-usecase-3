# Description
Combining duplicate statements with varying types and evidence.

# Code
```
import os
import unittest
from indra.preassembler import Preassembler
from indra.statements import *

def test_combine_duplicates():
    raf = Agent('RAF1')
    mek = Agent('MEK1')
    erk = Agent('ERK2')
    p1 = Phosphorylation(raf, mek,
            evidence=Evidence(text='foo'))
    p2 = Phosphorylation(raf, mek,
            evidence=Evidence(text='bar'))
    p3 = Phosphorylation(raf, mek,
            evidence=Evidence(text='baz'))
    p4 = Phosphorylation(raf, mek,
            evidence=Evidence(text='beep'))
    p5 = Phosphorylation(mek, erk,
            evidence=Evidence(text='foo2'))
    p6 = Dephosphorylation(mek, erk,
            evidence=Evidence(text='bar2'))
    p7 = Dephosphorylation(mek, erk,
            evidence=Evidence(text='baz2'))
    p8 = Dephosphorylation(mek, erk,
            evidence=Evidence(text='beep2'))
    p9 = Dephosphorylation(Agent('SRC'), Agent('KRAS'),
                           evidence=Evidence(text='beep'))
    stmts = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
    pa = Preassembler(bio_ontology, stmts=stmts)
    pa.combine_duplicates()
    # The statements come out sorted by their matches_key
    assert len(pa.unique_stmts) == 4, len(pa.unique_stmts)
    num_evs =[len(s.evidence) for s in pa.unique_stmts]
    assert pa.unique_stmts[0].matches(p6) # MEK dephos ERK
    assert num_evs[0] == 3, num_evs[0]
    assert pa.unique_stmts[1].matches(p9) # SRC dephos KRAS
    assert num_evs[1] == 1, num_evs[1]
    assert pa.unique_stmts[2].matches(p5) # MEK phos ERK
    assert num_evs[2] == 1, num_evs[2]
    assert pa.unique_stmts[3].matches(p1) # RAF phos MEK

```
