# Description
Make a request for a complex statement involving agents MEK@FPLX and ERK@FPLX.

# Code
```
import pytest
from indra.sources import indra_db_rest as dbr
from datetime import datetime

EXPECTED_BATCH_SIZE = 500

def __check_request(seconds, *args, **kwargs):
    check_stmts = kwargs.pop('check_stmts', True)
    now = datetime.now()
    resp = dbr.get_statements(*args, **kwargs)
    time_taken = datetime.now() - now
    if check_stmts:
        assert resp.statements, "Got no statements."

@pytest.mark.nonpublic
def test_request_for_complex():

```
