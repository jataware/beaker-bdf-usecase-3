# Description
Test the retrieval of protein expression data where one of the cell types is missing using the `context_client.get_protein_expression` method.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.databases import context_client
indra.util import unicode_strs

@pytest.mark.webservice
def test_get_protein_expression_cell_type_missing():
    protein_amounts = context_client.get_protein_expression(['EGFR'],
                                                            ['BT20_BREAST', 'XYZ'])
    assert 'BT20_BREAST' in protein_amounts
    assert protein_amounts['BT20_BREAST']['EGFR'] > 10000
    assert 'XYZ' in protein_amounts

```
