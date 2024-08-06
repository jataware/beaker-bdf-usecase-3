# Description
Example of getting identifier URL for CHEMBL.

# Code
```
import re

def test_chembl():
    cid = '1229517'
    assert get_identifiers_url('CHEMBL', cid) == \
        'https://identifiers.org/chembl.compound:CHEMBL%s' % cid
    assert get_identifiers_url('CHEMBL', 'CHEMBL%s' % cid) == \

```
