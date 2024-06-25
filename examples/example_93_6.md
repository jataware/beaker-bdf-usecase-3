# Description
Example of getting the latest standard URL for a given namespace and ID.

# Code
```
import re
from indra.databases.identifiers import get_identifiers_url

def test_get_identifiers_url():
    # Get latest standard URL for a given namespace and ID
    for ns_tuple, urls in ns_mapping.items():
        url = get_identifiers_url(*ns_tuple)

```
