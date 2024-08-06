# Description
Comparing the number of PubMed IDs returned for the same keyword with different search configurations using the `get_ids` method.

# Code
```
import time
from indra.literature import pubmed_client

@pytest.mark.webservice
def test_get_ids2():
    time.sleep(0.5)
    ids1 = pubmed_client.get_ids('JUN', use_text_word=False, reldate=365)
    ids2 = pubmed_client.get_ids('JUN', use_text_word=True, reldate=365)

```
