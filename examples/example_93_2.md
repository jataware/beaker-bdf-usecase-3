# Description
Example of mapping namespace and ID to standardized forms.

# Code
```
import re

def test_map_ns_id():
    assert get_ns_id_from_identifiers('uniprot', 'P12345') == \
        ('UP', 'P12345')
    assert get_ns_id_from_identifiers('go', 'GO:0005856') == \

```
