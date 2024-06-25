# Description
Fetching PubMed IDs using the `get_ids` method for a specific keyword search in the PubMed database.

# Code
```
import time
from indra.literature import pubmed_client

@pytest.mark.webservice
def test_get_ids1():
    time.sleep(0.5)
    ids = pubmed_client.get_ids('braf', retmax=10, db='pubmed')

```
