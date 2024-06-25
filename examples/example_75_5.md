# Description
Test if a request with no persistence times out correctly for agent NFkappaB@FPLX.

# Code
```
import pytest
from indra.sources import indra_db_rest as dbr
from datetime import datetime


@pytest.mark.nonpublic
def test_timeout_no_persist_nfkb():
    resp = dbr.get_statements(agents=["NFkappaB@FPLX"], persist=False, timeout=0)
    assert resp.is_working(), "Lookup resolved too fast."
    resp.wait_until_done(70)

```
