# Description
This example shows how to handle a nonexistent HGNC ID when retrieving an HGNC name with the `hgnc_client`.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.databases import hgnc_client
indra.util import unicode_strs

@pytest.mark.webservice
def test_get_hgnc_name_nonexistent():
    hgnc_id = '123456'
    hgnc_name = hgnc_client.get_hgnc_name(hgnc_id)
    assert hgnc_name is None

```
