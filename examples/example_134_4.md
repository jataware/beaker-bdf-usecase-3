# Description
Example of how to validate biological context using INDRA's validation functions, including handling invalid contexts and unknown namespaces.

# Code
```
import pytest
from indra.statements.validate import *

def test_context_validate():
    assert_valid_context(
        BioContext(organ=RefContext('liver', {'MESH': 'D008099'})))
    with pytest.raises(InvalidContext):
        assert_valid_context(BioContext())
    with pytest.raises(InvalidContext):
        assert_valid_context(BioContext(organ='liver'))
    with pytest.raises(UnknownNamespace):
        assert_valid_context(BioContext(organ=RefContext('liver',
                                                         db_refs={'XXX': '1'})))

```
