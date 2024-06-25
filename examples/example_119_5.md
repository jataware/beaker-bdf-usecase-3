# Description
Fetching PubMed IDs associated with a specific MeSH term using the `get_ids_for_mesh` method.

# Code
```
import time
from indra.literature import pubmed_client

@pytest.mark.webservice
def test_get_id_mesh():
    time.sleep(0.5)
    ids = pubmed_client.get_ids_for_mesh('D009101', reldate=365)
    assert len(ids) > 100, len(ids)
    ids_maj = pubmed_client.get_ids_for_mesh('D009101', major_topic=True,
                                             reldate=365)

```
