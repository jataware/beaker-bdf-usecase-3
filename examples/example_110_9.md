# Description
Attempt to process a private network from NDEx and expect an HTTPError

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
os
indra.sources.ndex_cx import process_ndex_network
requests.exceptions import HTTPError

@pytest.mark.webservice
def test_get_cx_from_ndex_unauth():
    # This network should error because unauthorized without username/pwd
    with pytest.raises(HTTPError):

```
