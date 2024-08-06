# Description
Testing for contradictions between statements.

# Code
```
import os
import unittest
from indra.preassembler import Preassembler
from indra.statements import *

def test_find_contradicts():
    st1 = Inhibition(Agent('a'), Agent('b'))
    st2 = Activation(Agent('a'), Agent('b'))
    st3 = IncreaseAmount(Agent('a'), Agent('b'))
    st4 = DecreaseAmount(Agent('a'), Agent('b'))
    st5 = ActiveForm(Agent('a',
            mods=[ModCondition('phosphorylation', None, None, True)]),
            'kinase', True)
    st6 = ActiveForm(Agent('a',
            mods=[ModCondition('phosphorylation', None, None, True)]),
            'kinase', False)
    pa = Preassembler(bio_ontology, [st1, st2, st3, st4, st5, st6])
    contradicts = pa.find_contradicts()
    assert len(contradicts) == 3
    for s1, s2 in contradicts:
        assert {s1.uuid, s2.uuid} in ({st1.uuid, st2.uuid},
                                      {st3.uuid, st4.uuid},

```
