# Description
Example of parsing the identifiers URL to extract namespace and ID.

# Code
```
import re
from indra.databases.identifiers import parse_identifiers_url

def test_parse_identifiers_url():
    # Get correct namespace and ID from standard and outdated URL formats
    for ns_tuple, urls in ns_mapping.items():
        for url in urls:
            ns, db_id = parse_identifiers_url(url)

```
