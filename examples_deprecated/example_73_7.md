# Description
Test for the activation and inhibition statements using `CxAssembler` to verify the generated CX model.

# Code
```
from indra.statements import *
from indra.assemblers.cx import CxAssembler

mek = Agent('MAP2K1', db_refs={'HGNC': '6840'})
erk = Agent('MAPK1', db_refs={'UP': 'P28482'})
dusp = Agent('DUSP4')
st_act = Activation(mek, erk)

def test_act():
    cxa = CxAssembler()
    cxa.add_statements([st_act, st_act2])
    cxa.make_model()
    assert len(cxa.cx['nodes']) == 3

```
