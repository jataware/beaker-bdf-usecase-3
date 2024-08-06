# Description
This example demonstrates how to use the `trrust` module from the `indra` library to fetch and process regulatory statements from the TRRUST web service. It verifies that more than 6200 regulatory statements are obtained and checks individual statement properties.

# Code
```
import pytest
from indra.sources import trrust

@pytest.mark.slow
@pytest.mark.webservice
def test_process_from_web():
    tp = trrust.process_from_web()
    assert len(tp.statements) > 6200
    for stmt in tp.statements:
        assert isinstance(stmt, RegulateAmount)
        assert len(stmt.evidence) == 1
        assert stmt.obj.db_refs.get('HGNC'), stmt.obj.db_refs
        assert stmt.subj.db_refs.get('HGNC'), stmt.subj.db_refs
        assert stmt.evidence[0].source_api == 'trrust'

```
