# Description
This example shows how to handle the absence of a UniProt ID for a given HGNC ID with the `hgnc_client`.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.databases import hgnc_client
indra.util import unicode_strs

def test_get_uniprot_id_none():
    # This HGNC entry doesn't have a UniProt ID
    hgnc_id = '37187'
    uniprot_id = hgnc_client.get_uniprot_id(hgnc_id)

```
