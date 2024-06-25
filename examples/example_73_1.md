# Description
Test for the phosphorylation statement using `CxAssembler` to verify the generated CX model.

# Code
```
from indra.statements import *
from indra.assemblers.cx import CxAssembler

mek = Agent('MAP2K1', db_refs={'HGNC': '6840'})
erk = Agent('MAPK1', db_refs={'UP': 'P28482'})

def test_phos():
    cxa = CxAssembler()
    cxa.add_statements([st_phos])
    cxa.make_model()
    assert len(cxa.cx['nodes']) == 2

```
