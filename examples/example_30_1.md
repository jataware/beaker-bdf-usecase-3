# Description
Get the citation count for a specific DOI using the COCI API.

# Code
```
from typing import Union
import requests
coci_url = 'https://opencitations.net/index/coci/api/v1/'

def get_citation_count_for_doi(doi: str) -> int:
    """Return the citation count for a given DOI.

    Note that the COCI API returns a count of 0 for DOIs that are not
    indexed.

    Parameters
    ----------
    doi :
        The DOI to get the citation count for.

    Returns
    -------
    :
        The citation count for the DOI.
    """

    url = citation_count_url + doi
    res = requests.get(url)
    res.raise_for_status()

```
