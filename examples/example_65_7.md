# Description
Test fetching profile data for BRAF and PTEN in CCLE study and verifying the data.

# Code
```
import pytest

@pytest.mark.webservice
def test_get_profile_data():
    profile_data = cbio_client.get_profile_data(cbio_client.ccle_study,
                                                ['BRAF', 'PTEN'],
                                                'COPY_NUMBER_ALTERATION',
                                                'all')
    assert profile_data['BT20_BREAST']['PTEN'] == -2
    assert profile_data['BT20_BREAST']['BRAF'] == 1
    assert profile_data['LOXIMVI_SKIN']['PTEN'] == 0
    assert profile_data['LOXIMVI_SKIN']['BRAF'] == 0

```
