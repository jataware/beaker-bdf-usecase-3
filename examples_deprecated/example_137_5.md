# Description
Test extracting of Complex statement from a text description of substances binding to each other.

# Code
```
import pytest
from indra.statements import *
from indra.sources.tees import api

@pytest.mark.slow
def test_process_bind():
    # Test extracting of Complex statement from a text description of
    # substances binding to each other.

    s = 'BRAF binds to p53.'
    tp = api.process_text(s)
    statements = tp.statements

    # There should be exactly one statement extracted
    assert len(statements) == 1
    statement0 = statements[0]

    # The statement should be of type Complex
    assert isinstance(statement0, Complex)

    # The members of the complex should correspond to the two substances
    # mentioned in the text
    members = statement0.members
    members = [m.db_refs['TEXT'] for m in members]
    assert len(members) == 2
    assert 'BRAF' in members
    assert 'p53' in members

    # is_direct should be true in evidence for bind statement
    assert len(statement0.evidence) == 1

```
