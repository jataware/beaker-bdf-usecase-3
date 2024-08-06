# Description
Standardize multiple genes to Agent instances using 'get_std_gene'.

# Code
```
os
indra.sources.gnbr.processor import *
indra.sources.gnbr.api as api

def test_multiple_genes():
    agents = get_std_gene('Erk1/2', '5594;5595')
    assert agents[0].name == 'MAPK1'
    assert agents[1].name == 'MAPK3'
    assert agents[0].db_refs['TEXT'] == 'Erk1/2'
    assert agents[1].db_refs['TEXT'] == 'Erk1/2'
    assert agents[0].db_refs['HGNC'] == '6871'

```
