# Description
Helper function to turn CSV rows into dictionaries from a given URL.

# Code
```
import sys
import requests
from io import StringIO, BytesIO

def load_lincs_csv(url):
    """Helper function to turn csv rows into dicts."""
    resp = requests.get(url, params={'output_type': '.csv'}, timeout=120)
    resp.raise_for_status()
    if sys.version_info[0] < 3:
        csv_io = BytesIO(resp.content)
    else:
        csv_io = StringIO(resp.text)
    data_rows = list(read_unicode_csv_fileobj(csv_io, delimiter=','))
    headers = data_rows[0]
    return [{header: val for header, val in zip(headers, line_elements)}

```
