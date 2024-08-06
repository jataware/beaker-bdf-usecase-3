# Description
Testing a complex title structure for a PubMed ID using the `get_title` method.

# Code
```
import time
from indra.literature import pubmed_client

@pytest.mark.webservice
def test_get_complex_title():
    time.sleep(0.5)
    title = pubmed_client.get_title('33463523')
    assert title
    assert title.lower().startswith('atomic structures')

```
