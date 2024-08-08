# Description
Test fetching CNA data for BRAF and AKT1 genes in specific cell lines and verifying the data.

# Code
```
import pytest

@pytest.mark.webservice
def test_get_ccle_cna():
    profile_data = cbio_client.get_ccle_cna(['BRAF', 'AKT1'],
                                            ['LOXIMVI_SKIN', 'SKMEL30_SKIN'])
    assert profile_data['SKMEL30_SKIN']['BRAF'] == 1
    assert profile_data['SKMEL30_SKIN']['AKT1'] == -1
    assert profile_data['LOXIMVI_SKIN']['BRAF'] == 0
    assert profile_data['LOXIMVI_SKIN']['AKT1'] == 0

```
