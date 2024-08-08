# Description
Test the OmniPath web API to ensure it is accessible and returns a successful response.

# Code
```
import requests

def test_omnipath_web_api():
    query_url = '%s/queries' % op_url
    res = requests.get(query_url)

```
