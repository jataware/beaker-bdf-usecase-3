# Description
Test for edge attributes using combined phosphorylation and dephosphorylation statements with `CxAssembler`.

# Code
```
from indra.statements import *
from indra.assemblers.cx import CxAssembler

mek = Agent('MAP2K1', db_refs={'HGNC': '6840'})
erk = Agent('MAPK1', db_refs={'UP': 'P28482'})
dusp = Agent('DUSP4')
st_phos = Phosphorylation(mek, erk)

def test_edge_attributes():
    cxa = CxAssembler()
    cxa.add_statements([st_phos, st_dephos])
    cxa.make_model()

```
