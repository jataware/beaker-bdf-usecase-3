# Description
Testing ID lookup with an invalid ID type and expecting a ValueError.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
import pytest

def test_invalid_idtype():
    with pytest.raises(ValueError):

```
