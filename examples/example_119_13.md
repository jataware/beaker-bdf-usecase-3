# Description
Attempting to get an abstract using the `get_abstract` method for a PubMed ID that might have no available abstract.

# Code
```
import time
from indra.literature import pubmed_client

@pytest.mark.webservice
def test_get_no_abstract():
    time.sleep(0.5)
    abstract = pubmed_client.get_abstract('xx')

```
