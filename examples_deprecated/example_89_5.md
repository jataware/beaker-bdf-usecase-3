# Description
This example demonstrates how to convert an Entrez ID to an HGNC ID using the `hgnc_client`.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.databases import hgnc_client
indra.util import unicode_strs

def test_entrez_hgnc():
    entrez_id = '653509'
    hgnc_id = hgnc_client.get_hgnc_from_entrez(entrez_id)

```
