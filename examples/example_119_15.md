# Description
Fetching metadata for multiple PubMed IDs using the `get_metadata_for_ids` method and checking the type of author data.

# Code
```
import time
from indra.literature import pubmed_client

@pytest.mark.webservice
def test_get_metadata_for_ids():
    time.sleep(0.5)
    pmids1 = ['27123883', '27121204', '27115606']
    metadata1 = pubmed_client.get_metadata_for_ids(pmids1)
    pmids2 = ['27123883']
    time.sleep(0.5)
    metadata2 = pubmed_client.get_metadata_for_ids(pmids2,
                                                   detailed_authors=True)
    assert all(isinstance(a, str) for a in metadata1[pmids1[0]]['authors'])
    assert all(isinstance(a, dict) for a in metadata2[pmids2[0]]['authors'])
    assert metadata1[pmids1[0]]['authors'][0] == 'Le Rhun'
    assert metadata2[pmids1[0]]['authors'][0]['last_name'] == 'Le Rhun'
    assert 'Lille' in \

```
