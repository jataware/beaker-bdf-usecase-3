# Description
Check that a null request raises the correct exception.

# Code
```
import pytest

@pytest.mark.nonpublic
def test_null_request():
    try:
        dbr.get_statements()
    except ValueError:
        return
    except BaseException as e:
        assert False, "Raised wrong exception: " + str(e)

```
