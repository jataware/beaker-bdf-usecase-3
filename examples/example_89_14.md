# Description
This example demonstrates how to convert an MGI name to an HGNC ID and name using the `hgnc_client`.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.databases import hgnc_client
indra.util import unicode_strs

def test_mgi_name_conversion():
    assert hgnc_client.get_hgnc_id_from_mgi_name('Braf') == '1097'

```
