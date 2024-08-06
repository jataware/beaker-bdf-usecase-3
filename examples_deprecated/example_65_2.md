# Description
Test fetching cancer types for 'lung' and ensuring the data is retrieved correctly.

# Code
```
import pytest

@pytest.mark.webservice
def test_get_cancer_types():
    type_ids = cbio_client.get_cancer_types('lung')

```
