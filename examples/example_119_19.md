# Description
Handling embedded HTML in abstracts fetched using the `get_abstract` method.

# Code
```
import time
from indra.literature import pubmed_client

@pytest.mark.webservice
def test_abstract_with_html_embedded():
    time.sleep(0.5)
    res = pubmed_client.get_abstract('25484845')

```
