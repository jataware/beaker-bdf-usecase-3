# Description
Test the retrieval of mutations data where one of the genes is missing using the `context_client.get_mutations` method.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.databases import context_client
indra.util import unicode_strs

@pytest.mark.webservice
def test_get_mutations_gene_missing():
    mutations = context_client.get_mutations(['BRAF', 'XYZ'], ['A375_SKIN'])
    assert 'A375_SKIN' in mutations
    assert mutations['A375_SKIN']['BRAF'] == ['V600E']

```
