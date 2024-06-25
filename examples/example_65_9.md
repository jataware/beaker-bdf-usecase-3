# Description
Test fetching mRNA data for specific genes in cell lines and verifying the data.

# Code
```
import pytest

@pytest.mark.webservice
def test_get_ccle_mrna():
    mrna = cbio_client.get_ccle_mrna(['XYZ', 'MAP2K1'], ['A375_SKIN'])
    assert 'A375_SKIN' in mrna
    assert mrna['A375_SKIN'] is not None
    assert mrna['A375_SKIN']['MAP2K1'] > 10
    assert mrna['A375_SKIN']['XYZ'] is None
    mrna = cbio_client.get_ccle_mrna(['EGFR', 'BRAF'], ['XXX'])
    assert 'XXX' in mrna

```
