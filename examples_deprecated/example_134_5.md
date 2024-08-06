# Description
Example of how to validate evidence using INDRA's validation functions, with cases handling invalid text references and unknown namespaces.

# Code
```
import pytest
from indra.statements.validate import *

def test_evidence_validate():
    assert_valid_evidence(Evidence(pmid='1234'))
    with pytest.raises(InvalidTextRefs):
        assert_valid_evidence(Evidence(pmid=None, text_refs={'PMID': '1234'}))
    with pytest.raises(UnknownNamespace):
        assert_valid_evidence(Evidence(context=BioContext(

```
