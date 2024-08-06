# Description
Test the _listify function in the INDRA BioPAX processor module.

# Code
```
import pytest

def test_listify():
    assert bpc._listify(1) == [1]
    assert bpc._listify([1,2] == [1,2])

```
