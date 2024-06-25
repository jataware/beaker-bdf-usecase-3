# Description
Getting the count of PubMed IDs for given search terms using the `get_id_count` method.

# Code
```
import time
from indra.literature import pubmed_client

@pytest.mark.webservice
def test_get_id_count():
    time.sleep(0.5)
    id_count = pubmed_client.get_id_count('SDLFKJSLDKJH')
    assert id_count == 0
    id_count = pubmed_client.get_id_count('KRAS')

```
