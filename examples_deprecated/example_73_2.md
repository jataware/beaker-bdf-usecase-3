# Description
Test for the phosphorylation statement using `NiceCxAssembler` to verify the generated NiceCX model.

# Code
```
from indra.statements import *
from indra.assemblers.cx import NiceCxAssembler

mek = Agent('MAP2K1', db_refs={'HGNC': '6840'})
erk = Agent('MAPK1', db_refs={'UP': 'P28482'})

def test_phos_nice():
    cxa = NiceCxAssembler([st_cited])
    cxa.make_model()
    assert len(cxa.network.nodes) == 2
    assert len(cxa.network.edges) == 1

```
