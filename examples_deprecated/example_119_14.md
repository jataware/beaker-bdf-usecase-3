# Description
Retrieving PubMed IDs related to a specific gene using the `get_ids_for_gene` method.

# Code
```
import time
from indra.literature import pubmed_client

@pytest.mark.webservice
def test_get_ids_for_gene():
    time.sleep(0.5)
    ids = pubmed_client.get_ids_for_gene('EXOC1')

```
