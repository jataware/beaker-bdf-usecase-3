# Description
Fetching zero PubMed IDs using the `get_ids` method when no results are found for a specific keyword.

# Code
```
import time
from indra.literature import pubmed_client

@pytest.mark.webservice
def test_get_no_ids():
    time.sleep(0.5)
    ids = pubmed_client.get_ids('UUuXNWMCusRpcVTX', retmax=10, db='pubmed')

```
