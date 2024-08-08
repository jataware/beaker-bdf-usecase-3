# Description
Retrieving and asserting a PubMed article title using the `get_title` method.

# Code
```
import time
from indra.literature import pubmed_client

@pytest.mark.webservice
def test_get_title():
    time.sleep(0.5)
    title = pubmed_client.get_title('27754804')
    assert title

```
