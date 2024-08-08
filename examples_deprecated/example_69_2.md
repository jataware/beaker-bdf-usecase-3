# Description
Test the retrieval of mutations data for specific genes and cell types using the `context_client.get_mutations` method.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.databases import context_client
indra.util import unicode_strs

@pytest.mark.webservice
def test_get_mutations():
    res = context_client.get_mutations(['BRAF'], ['A375_SKIN'])
    assert res is not None
    assert res.get('A375_SKIN') is not None
    assert res['A375_SKIN'].get('BRAF') is not None
    assert res['A375_SKIN']['BRAF'] == ['V600E']

```
