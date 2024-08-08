# Description
This example shows how to handle an invalid Entrez ID when converting it to an HGNC ID with the `hgnc_client`.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.databases import hgnc_client
indra.util import unicode_strs

def test_entrez_hgnc_none():
    entrez_id = 'xxx'
    hgnc_id = hgnc_client.get_hgnc_from_entrez(entrez_id)

```
