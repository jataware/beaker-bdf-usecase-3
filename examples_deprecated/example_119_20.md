# Description
Fetching the abstract for a specific PubMed ID and its metadata, ensuring the abstract length exceeds a threshold.

# Code
```
import time
from indra.literature import pubmed_client

@pytest.mark.webservice
def test_pmid_27821631():
    time.sleep(0.5)
    pmid = '27821631'
    res = pubmed_client.get_abstract(pmid)
    assert len(res) > 50, res
    res = pubmed_client.get_metadata_for_ids([pmid], get_abstracts=True)
    assert res[pmid]['title'] is not None

```
