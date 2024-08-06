# Description
This example demonstrates how to retrieve a UniProt ID using an HGNC ID with the `hgnc_client`.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.databases import hgnc_client
indra.util import unicode_strs

def test_get_uniprot_id():
    hgnc_id = '6840'
    uniprot_id = hgnc_client.get_uniprot_id(hgnc_id)
    assert uniprot_id == 'Q02750'

```
