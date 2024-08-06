# Description
Test regulating amount statements with proper source counts.

# Code
```
import pytest

@pytest.mark.nonpublic
def test_regulate_amount():
    idbp = dbr.get_statements('FOS', stmt_type='RegulateAmount')
    stmts = idbp.statements
    stmt_types = {type(s).__name__ for s in stmts}
    counts = idbp.get_source_counts()
    one_key = list(counts.keys())[0]
    assert counts[one_key] == idbp.get_source_count_by_hash(one_key)
    assert {'IncreaseAmount', 'DecreaseAmount'}.issubset(stmt_types), \

```
