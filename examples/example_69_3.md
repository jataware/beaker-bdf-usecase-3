# Description
Test the retrieval of protein expression data where one of the genes is missing using the `context_client.get_protein_expression` method.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.databases import context_client
indra.util import unicode_strs

@pytest.mark.webservice
def test_get_protein_expression_gene_missing():
    protein_amounts = context_client.get_protein_expression(['EGFR', 'XYZ'],
                                                            ['BT20_BREAST'])
    assert 'BT20_BREAST' in protein_amounts
    assert protein_amounts['BT20_BREAST']['EGFR'] > 10000

```
