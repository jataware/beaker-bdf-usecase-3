# Description
This example demonstrates how to retrieve an HGNC name using an HGNC ID with the `hgnc_client`.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.databases import hgnc_client
indra.util import unicode_strs

def test_get_hgnc_name():
    hgnc_id = '3236'
    hgnc_name = hgnc_client.get_hgnc_name(hgnc_id)
    assert hgnc_name == 'EGFR'

```
