# Description
Attempting to send an invalid request using the `send_request` method to ensure proper handling of incorrect URLs.

# Code
```
import time
from indra.literature import pubmed_client

@pytest.mark.webservice
def test_send_request_invalid():
    time.sleep(0.5)
    res = pubmed_client.send_request('http://xxxxxxx', data={})

```
