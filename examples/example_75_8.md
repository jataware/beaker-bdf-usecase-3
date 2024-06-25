# Description
Test retrieval of statements by providing their hashes.

# Code
```
import pytest

@pytest.mark.nonpublic
def test_get_statements_by_hash():
    hash_list = [30674674032092136, -22289282229858243, -25056605420392180]
    p = dbr.get_statements_by_hash(hash_list)
    stmts = p.statements
    print({s.get_hash(shallow=True): s for s in stmts})
    assert len(stmts) >= 2, \
        "Wrong number of statements: %s vs. %s" % (len(stmts), len(hash_list))

    p = dbr.get_statements_by_hash(hash_list)
    assert len(p.statements)
    assert len(p.get_source_counts())

```
