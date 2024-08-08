# Description
This example demonstrates how to retrieve an HGNC ID from a Mouse ID using the `hgnc_client`.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.databases import hgnc_client
indra.util import unicode_strs

def test_mouse_map():
    hgnc_id1 = hgnc_client.get_hgnc_from_mouse('109599')
    hgnc_id2 = hgnc_client.get_hgnc_from_mouse('MGI:109599')
    assert hgnc_id1 == '4820'
    assert hgnc_id2 == '4820'
    hgnc_id = hgnc_client.get_hgnc_from_mouse('xxx')

```
