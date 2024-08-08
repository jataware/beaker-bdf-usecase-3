# Description
Test statement retrieval via paper-specific queries.

# Code
```
import pytest

@pytest.mark.nonpublic
@pytest.mark.nogha
def test_paper_query():
    p = dbr.get_statements_for_papers([('pmcid', 'PMC5770457'),
                                       ('pmid', '27014235')])
    stmts_1 = p.statements
    assert len(stmts_1)

    p = dbr.get_statements_for_papers([('pmcid', 'PMC5770457'),
                                       ('pmid', '27014235')])
    assert len(p.statements)
    assert len(p.get_source_counts())

```
