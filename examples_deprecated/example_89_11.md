# Description
This example demonstrates how to get the current HGNC ID for a given symbol, handling both current and outdated symbols using the `hgnc_client`.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.databases import hgnc_client
indra.util import unicode_strs

def test_get_current_id():
    # Current symbol
    assert hgnc_client.get_current_hgnc_id('BRAF') == '1097'
    # Outdated symbol, one ID
    assert hgnc_client.get_current_hgnc_id('SEPT7') == '1717'
    # Outdated symbol, multiple IDs
    ids = hgnc_client.get_current_hgnc_id('HOX1')
    assert len(ids) == 10

```
