# Description
Test valid MONDO ID lookup by name

# Code
```
from indra.databases import mondo_client
EXAMPLE_NAME = 'tenosynovial giant cell tumor, localized type'

def test_mondo_id_lookup():
    name = mondo_client.get_name_from_id(EXAMPLE_ID)
    assert name is not None

```
