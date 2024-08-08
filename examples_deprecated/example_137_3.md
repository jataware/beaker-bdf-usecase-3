# Description
Test extraction of IncreaseAmount statements from a text description of a substance increasing the expression of some gene.

# Code
```
import pytest
from indra.statements import *
from indra.sources.tees import api

@pytest.mark.slow
def test_process_increase_amount():
    # Test extraction of IncreaseAmount statements from a text description
    # of a substance increasing the expression of some gene.

    s = 'BRAF increases the expression of p53.'

    tp = api.process_text(s)
    statements = tp.statements

    # Exactly one statement should have been extracted from the provided text
    assert len(statements) == 1
    statement0 = statements[0]

    # The statement should be of type IncreaseAmount
    assert isinstance(statement0, IncreaseAmount)

    # The subject and object in the statement should correspond with what is
    # in the text
    subj0 = statement0.subj.db_refs['TEXT']
    assert subj0 == 'BRAF'
    #
    obj0 = statement0.obj.db_refs['TEXT']
    assert obj0 == 'p53'

    # There should be an evidence object (properties of evidence tested in
    # other tests)

```
