# Description
Expanding a page range notation using the `expand_pagination` method.

# Code
```
import time
from indra.literature import pubmed_client

@pytest.mark.webservice
def test_expand_pagination():
    time.sleep(0.5)
    pages = '456-7'
    new_pages = pubmed_client.expand_pagination(pages)

```
