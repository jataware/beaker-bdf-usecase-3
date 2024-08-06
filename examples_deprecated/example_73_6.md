# Description
Test for the more complex statement using `CxAssembler` to verify the generated CX model when duplicated elements are present.

# Code
```
from indra.statements import *
from indra.assemblers.cx import CxAssembler

mek = Agent('MAP2K1', db_refs={'HGNC': '6840'})
erk = Agent('MAPK1', db_refs={'UP': 'P28482'})
dusp = Agent('DUSP4')

def test_complex2():
    cxa = CxAssembler()
    cxa.add_statements([st_complex2])
    cxa.make_model()
    assert len(cxa.cx['nodes']) == 3

```
