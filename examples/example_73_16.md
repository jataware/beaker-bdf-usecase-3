# Description
Test for creating and printing the model using `CxAssembler`.

# Code
```
from indra.statements import *
from indra.assemblers.cx import CxAssembler

mek = Agent('MAP2K1', db_refs={'HGNC': '6840'})
erk = Agent('MAPK1', db_refs={'UP': 'P28482'})

def test_make_print_model():
    cxa = CxAssembler()
    cxa.add_statements([st_phos])
    cx_str = cxa.make_model()

```
