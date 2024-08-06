# Description
Testing the sorting of combined duplicate statements.

# Code
```
import os
import unittest
from indra.preassembler import Preassembler
from indra.statements import *

def test_duplicates_sorting():
    mc = ModCondition('phosphorylation')
    map2k1_1 = Agent('MAP2K1', mods=[mc])
    mc1 = ModCondition('phosphorylation', 'serine', '218')
    mc2 = ModCondition('phosphorylation', 'serine', '222')
    mc3 = ModCondition('phosphorylation', 'serine', '298')
    map2k1_2 = Agent('MAP2K1', mods=[mc1, mc2, mc3])
    mapk3 = Agent('MAPK3')
    st1 = Phosphorylation(map2k1_1, mapk3, position='218')
    st2 = Phosphorylation(map2k1_2, mapk3)
    st3 = Phosphorylation(map2k1_1, mapk3, position='218')
    stmts = [st1, st2, st3]
    pa = Preassembler(bio_ontology, stmts=stmts)
    pa.combine_duplicates()

```
