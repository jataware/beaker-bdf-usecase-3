# Description
Test fetching cancer studies for 'paad' and ensuring the data is retrieved correctly.

# Code
```
import pytest

@pytest.mark.webservice
def test_get_cancer_studies():
    study_ids = cbio_client.get_cancer_studies('paad')
    assert len(study_ids) > 0

```
