# Description
Test whether the pmid provided to the TEES processor is put into the statement's evidence.

# Code
```
import pytest
from indra.statements import *
from indra.sources.tees import api

@pytest.mark.slow
def test_evidence_pmid():
    # Test whether the pmid provided to the TEES processor is put into the
    # statement's evidence

    pmid = '42'

    # Process some text
    s = 'BRAF binds to p53.'
    tp = api.process_text(s, pmid)
    statements = tp.statements

    # Verify that the pmid was put in the right place
    assert len(statements[0].evidence) == 1

```
