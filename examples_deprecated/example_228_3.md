# Description
Test retrieving MONDO ID from label

# Code
```
from indra.databases import mondo_client
EXAMPLE_NAME = 'tenosynovial giant cell tumor, localized type'

def test_mondo_label_to_id():
    identifier = mondo_client.get_id_from_name(EXAMPLE_NAME)
    assert identifier is not None

```
