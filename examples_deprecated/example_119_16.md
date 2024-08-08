# Description
Fetching paper references included in PubMed metadata using the `get_metadata_for_ids` method with detailed reference inclusion.

# Code
```
import time
from indra.literature import pubmed_client

@pytest.mark.webservice
def test_get_paper_references():
    time.sleep(0.5)
    pmids = ['27123883', '27121204', '27115606']
    test_pmid = '27121204'
    referenced_pmid = '25439075'
    metadata_1 = pubmed_client.get_metadata_for_ids(pmids, references_included='pmid')
    assert len(metadata_1[test_pmid]['references']) != 0
    assert metadata_1[test_pmid]['references'][0] == referenced_pmid

    metadata_2 = pubmed_client.get_metadata_for_ids(pmids, references_included='detailed')
    assert len(metadata_2[test_pmid]['references']) != 0

```
