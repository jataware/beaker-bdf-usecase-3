# Description
Retrieving the abstract of a PubMed article without prepending the title using the `get_abstract` method.

# Code
```
import time
from indra.literature import pubmed_client

@pytest.mark.webservice
def test_get_abstract_notitle():
    time.sleep(0.5)
    abstract = pubmed_client.get_abstract('27754804', prepend_title=False)
    assert abstract.startswith('The RAF inhibitor')

```
