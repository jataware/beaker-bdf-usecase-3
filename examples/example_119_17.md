# Description
Retrieving publication dates for multiple PubMed IDs using the `get_metadata_for_ids` method and verifying the dates.

# Code
```
import time
from indra.literature import pubmed_client

@pytest.mark.webservice
def test_get_pub_date():
    time.sleep(0.5)
    pmids = ['27123883', '27121204', '27115606']
    metadata = pubmed_client.get_metadata_for_ids(pmids)
    assert metadata[pmids[0]]['publication_date']['year'] == 2016
    assert metadata[pmids[0]]['publication_date']['month'] == 4
    assert metadata[pmids[0]]['publication_date']['day'] == 29
    assert metadata[pmids[1]]['publication_date']['year'] == 2016
    assert metadata[pmids[1]]['publication_date']['month'] == 4
    assert metadata[pmids[1]]['publication_date']['day'] == 29
    assert metadata[pmids[2]]['publication_date']['year'] == 2016
    assert metadata[pmids[2]]['publication_date']['month'] == 4

```
