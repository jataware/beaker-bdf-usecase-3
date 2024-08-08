# Description
This example demonstrates how to convert an Ensembl ID to an HGNC ID and back using the `hgnc_client`.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.databases import hgnc_client
indra.util import unicode_strs

def test_ensembl_hgnc():
    ensembl_id = 'ENSG00000006071'
    hgnc_id = hgnc_client.get_hgnc_from_ensembl(ensembl_id)
    assert hgnc_id == '59', hgnc_id

```
