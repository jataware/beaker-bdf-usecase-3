# Description
Example of checking if namespace is embedded.

# Code
```
import re

def test_namespace_embedded():
    assert namespace_embedded('CHEBI') is True
    assert namespace_embedded('GO') is True
    assert namespace_embedded('EFO') is False

```
