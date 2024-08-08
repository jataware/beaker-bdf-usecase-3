# Description
Example of how to validate text references (text_refs) with expected invalid and valid scenarios, specifically using INDRA's validation functions.

# Code
```
import pytest

def test_text_refs_validate():
    with pytest.raises(InvalidTextRefs):
        assert_valid_text_refs({'pmid': '123'})
    with pytest.raises(InvalidTextRefs):
        assert_valid_text_refs({'PMID': 'api123'})
    with pytest.raises(InvalidTextRefs):
        assert_valid_text_refs({'DOI': 'https://xyz'})
    with pytest.raises(InvalidTextRefs):
        assert_valid_text_refs({'PMCID': '12345'})
    assert_valid_text_refs({'PMID': '12345'})
    assert_valid_text_refs({'PMCID': 'PMC12345'})

```
