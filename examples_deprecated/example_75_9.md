# Description
Test the strict stop mechanism using a short timeout.

# Code
```
import pytest
from indra.sources import indra_db_rest as dbr
from datetime import datetime

def test_get_statements_strict_stop_short():
    start = datetime.now()
    p = dbr.get_statements("TNF", timeout=1, strict_stop=True)
    end = datetime.now()
    sleep(5)
    assert not p.is_working()
    dt = (end - start).total_seconds()
    assert 1 <= dt < 1.5, dt
    assert not p.statements

```
