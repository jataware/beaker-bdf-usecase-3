# Description
Test for cited statements using `CxAssembler` to verify citations in the generated CX model.

# Code
```
from indra.statements import *
from indra.assemblers.cx import CxAssembler

mek = Agent('MAP2K1', db_refs={'HGNC': '6840'})
erk = Agent('MAPK1', db_refs={'UP': 'P28482'})

def test_cited():
    cxa = CxAssembler()
    cxa.add_statements([st_cited])
    cxa.make_model()
    assert len(cxa.cx['citations']) == 1
    assert len(cxa.cx['edgeCitations']) == 1
    citation = cxa.cx['citations'][0]
    assert citation.get('dc:identifier') == 'pmid:12345'
    cid = citation.get('@id')
    assert cxa.cx['edgeCitations'][0]['citations'][0] == cid

```
