# Description
Fetching a PubMed ID from the database PMC using the `get_ids` method for a specific keyword search.

# Code
```
import time
from indra.literature import pubmed_client

@pytest.mark.webservice
def test_get_pmc_ids():
    time.sleep(0.5)
    ids = pubmed_client.get_ids('braf', retmax=10, db='pmc')

```
