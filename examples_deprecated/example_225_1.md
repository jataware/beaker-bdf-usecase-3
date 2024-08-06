# Description
Test to check if the DOID client is correctly loaded.

# Code
```
from indra.databases import doid_client

def test_doid_client_loaded():
    assert 'doid' == client.prefix
    assert client.entries

```
