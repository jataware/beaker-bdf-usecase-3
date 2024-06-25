# Description
This example demonstrates how to handle enzyme codes and their corresponding HGNC IDs using the `hgnc_client`.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.databases import hgnc_client
indra.util import unicode_strs

def test_ec_code():
    assert not hgnc_client.get_enzymes("41022"), "RNA is not an enzyme"
    assert "41022" not in hgnc_client.get_hgncs_from_enzyme('2.4.1.228')
    assert "2.4.1.228" in hgnc_client.get_enzymes('18149')

```
