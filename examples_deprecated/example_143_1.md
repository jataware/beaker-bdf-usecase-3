# Description
Processing data from web using 'virhostnet.process_from_web' function and validating the statements retrieved.

# Code
```
import pytest
from indra.statements import Complex

@pytest.mark.webservice
@pytest.mark.slow
def test_process_from_web():
    vp = virhostnet.process_from_web(query='pubmed:8553588')
    assert len(vp.statements) == 5, len(vp.statements)
    assert all(isinstance(st, Complex) for st in vp.statements)
    assert all(stmt.members[1].db_refs['REFSEQ_PROT'] == 'NP_040311'
               for stmt in vp.statements)
    assert all(stmt.evidence[0].pmid == '8553588'

```
