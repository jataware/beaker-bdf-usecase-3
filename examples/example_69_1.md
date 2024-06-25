# Description
Test the retrieval of protein expression data for specific genes and cell types using the `context_client.get_protein_expression` method.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.databases import context_client
indra.util import unicode_strs

@pytest.mark.webservice
def test_get_protein_expression():
    res = context_client.get_protein_expression(['EGFR'], ['BT20_BREAST'])
    assert res is not None
    assert res.get('BT20_BREAST') is not None
    assert res['BT20_BREAST'].get('EGFR') is not None
    assert res['BT20_BREAST']['EGFR'] > 1000

```
