# Description
Handling the provided PubMed ID prefixed with 'PMID' using the `get_title` method.

# Code
```
import time
from indra.literature import pubmed_client

@pytest.mark.webservice
def test_get_title_prefix():
    time.sleep(0.5)
    title = pubmed_client.get_title('PMID27754804')
    assert title

```
