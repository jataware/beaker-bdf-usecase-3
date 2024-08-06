# Description
Test for invalid cited statements using `CxAssembler` to ensure no invalid citations are present in the generated CX model.

# Code
```
from indra.statements import *
from indra.assemblers.cx import CxAssembler

mek = Agent('MAP2K1', db_refs={'HGNC': '6840'})
erk = Agent('MAPK1', db_refs={'UP': 'P28482'})

def test_invalid_cited():
    cxa = CxAssembler()
    cxa.add_statements([st_invalid_cited])
    cxa.make_model()
    assert not cxa.cx['citations']

```
