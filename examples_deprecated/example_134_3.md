# Description
Example of how to validate PMID text references within Evidence objects using INDRA's validation functions.

# Code
```
import pytest
from indra.statements.validate import *

def test_pmid_text_refs_validate():
    assert_valid_pmid_text_refs(Evidence(pmid=None))
    assert_valid_pmid_text_refs(Evidence(pmid='1234'))
    assert_valid_pmid_text_refs(Evidence(pmid='1234',
                                         text_refs={'PMID': '1234'}))
    with pytest.raises(InvalidTextRefs):
        assert_valid_pmid_text_refs(Evidence(pmid='1234',
                                             text_refs={'PMID': '12345'}))
    with pytest.raises(InvalidTextRefs):
        assert_valid_pmid_text_refs(Evidence(pmid=None,

```
