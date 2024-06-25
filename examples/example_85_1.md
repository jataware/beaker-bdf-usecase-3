# Description
Standardize a gene to an Agent instance using 'get_std_gene'.

# Code
```
os
indra.sources.gnbr.processor import *
indra.sources.gnbr.api as api

def test_standardize_agent():
    agent = get_std_gene('xxx', '673')
    assert isinstance(agent[0], Agent)
    assert agent[0].name == 'BRAF'
    assert agent[0].db_refs.get('TEXT') == 'xxx'
    assert agent[0].db_refs.get('EGID') == '673'

```
