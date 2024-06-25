# Description
This example demonstrates how to get the gene type for a given HGNC ID using the `hgnc_client`.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.databases import hgnc_client
indra.util import unicode_strs

def test_gene_type():
    assert hgnc_client.get_gene_type('1097') == 'gene with protein product'

```
