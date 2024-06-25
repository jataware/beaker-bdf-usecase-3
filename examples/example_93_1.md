# Description
Example of mapping namespace identifiers to their standard forms.

# Code
```
import re

def test_map_ns():
    assert get_ns_from_identifiers('go') == 'GO'
    assert get_ns_from_identifiers('uniprot') == 'UP'

```
