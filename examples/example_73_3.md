# Description
Test for GEF and GAP statements using `NiceCxAssembler` to verify the generated NiceCX model.

# Code
```
from indra.statements import *
from indra.assemblers.cx import NiceCxAssembler

st_gef = Gef(Agent('SOS1'), Agent('HRAS'))

def test_gapgef_nice():
    cxa = NiceCxAssembler([st_gef, st_gap])
    cxa.make_model()
    assert len(cxa.network.nodes) == 3, cxa.network.nodes
    assert len(cxa.network.edges) == 2

```
