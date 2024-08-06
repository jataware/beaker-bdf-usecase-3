# Description
Test the extraction of phosphorylation with a simple example.

# Code
```
import pytest
from indra.statements import *
from indra.sources.tees import api

@pytest.mark.slow
def test_process_phosphorylation():
    # Test the extraction of phosphorylation with a simple example.
    s = 'Ras leads to the phosphorylation of Braf.'
    tp = api.process_text(s)
    statements = tp.statements

    # Should only extract one statement
    assert len(statements) == 1

    # The statement should be a Phosphorylation statement
    statement = statements[0]
    assert isinstance(statement, Phosphorylation)

    # Check that the enzyme and substrate of the statement match the text
    enz = statement.enz
    assert enz.db_refs['TEXT'] == 'Ras'
    #
    sub = statement.sub
    assert sub.db_refs['TEXT'] == 'Braf'

    # There should be an evidence object (properties of evidence tested in
    # other tests)

```
