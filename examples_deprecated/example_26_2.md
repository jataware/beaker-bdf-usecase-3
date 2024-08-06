# Description
Retrieve the JSON record for a given PubChem CID.

# Code
```
import logging
import requests
from functools import lru_cache


@lru_cache(maxsize=5000)
def get_json_record(pubchem_cid):
    """Return the JSON record of a given PubChem CID.

    Parameters
    ----------
    pubchem_cid : str
        The PubChem CID whose record should be returned.

    Returns
    -------
    dict
        The record deserialized from JSON.
    """
    url = (pubchem_url + '_view/data/compound/%s/JSON/') % pubchem_cid
    res = requests.get(url)

```
