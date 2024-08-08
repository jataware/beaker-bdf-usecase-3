# Description
Get the MESH label for a given MESH ID using the NLM REST API.

# Code
```
import requests
from functools import lru_cache

@lru_cache(maxsize=1000)
def get_mesh_name_from_web(mesh_id):
    """Get the MESH label for the given MESH ID using the NLM REST API.

    Parameters
    ----------
    mesh_id : str
        MESH Identifier, e.g. 'D003094'.

    Returns
    -------
    str
        Label for the MESH ID, or None if the query failed or no label was
        found.
    """
    url = MESH_URL + mesh_id + '.json'
    resp = requests.get(url)
    if resp.status_code != 200:
        return None
    mesh_json = resp.json()
    try:
        label = mesh_json['label']['@value']
    except (KeyError, IndexError, TypeError) as e:
        return None

```
