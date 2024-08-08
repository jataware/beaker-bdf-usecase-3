# Description
Retrieving the abstract of a PubMed article with the title prepended using the `get_abstract` method.

# Code
```
import time
from indra.literature import pubmed_client

@pytest.mark.webservice
def test_get_abstract_title():
    time.sleep(0.5)
    abstract = pubmed_client.get_abstract('27754804', prepend_title=True)
    assert abstract.lower().startswith('targeting autophagy')

```
