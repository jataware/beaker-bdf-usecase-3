# Description
Test fetching the number of sequenced cases for 'paad_tcga' and ensuring the data is retrieved correctly.

# Code
```
import pytest

@pytest.mark.webservice
def test_get_num_sequenced():
    num_case = cbio_client.get_num_sequenced('paad_tcga')

```
