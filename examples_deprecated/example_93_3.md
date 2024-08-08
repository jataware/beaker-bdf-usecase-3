# Description
Example of getting the identifiers namespace.

# Code
```
import re

def test_identifiers_ns():
    assert get_identifiers_ns('UP') == 'uniprot'
    assert get_identifiers_ns('GO') == 'go'

```
