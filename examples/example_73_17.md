# Description
Test for no PMIDs in citations using `CxAssembler`.

# Code
```
from indra.statements import *
from indra.assemblers.cx import CxAssembler

mek = Agent('MAP2K1', db_refs={'HGNC': '6840'})
erk = Agent('MAPK1', db_refs={'UP': 'P28482'})

def test_no_pmid():
    cxa = CxAssembler([st_not_cited])
    cxa.make_model()

```
