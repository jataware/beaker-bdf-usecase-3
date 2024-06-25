# Description
Example of ensuring prefix if needed in identifiers.

# Code
```
import re

def test_ensure_prefix_if_needed():
    assert ensure_prefix_if_needed('CHEBI', 'CHEBI:123') == 'CHEBI:123'
    assert ensure_prefix_if_needed('CHEBI', '123') == 'CHEBI:123'
    assert ensure_prefix_if_needed('GO', '00004') == 'GO:00004'
    assert ensure_prefix_if_needed('EFO', '1234') == '1234'

```
