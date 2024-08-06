# Description
This example demonstrates how to retrieve an HGNC ID from a Rat ID using the `hgnc_client`.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.databases import hgnc_client
indra.util import unicode_strs

def test_rat_map():
    hgnc_id1 = hgnc_client.get_hgnc_from_rat('6496784')
    hgnc_id2 = hgnc_client.get_hgnc_from_rat('RGD:6496784')
    assert hgnc_id1 == '44155'
    assert hgnc_id2 == '44155'
    hgnc_id = hgnc_client.get_hgnc_from_rat('xxx')

```
