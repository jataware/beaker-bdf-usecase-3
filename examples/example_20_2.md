# Description
Get the MESH label for a given MESH ID using local mappings and fallback to the NLM REST API if not found locally.

# Code
```
import requests
from functools import lru_cache
MESH_URL = 'https://id.nlm.nih.gov/mesh/'
mesh_id_to_name = {}
def get_mesh_name_from_web(mesh_id):
    url = MESH_URL + mesh_id + '.json'
    resp = requests.get(url)
    if resp.status_code != 200:
        return None
    mesh_json = resp.json()
    try:
        label = mesh_json['label']['@value']
    except (KeyError, IndexError, TypeError):
        return None

def get_mesh_name(mesh_id, offline=False):
    """Get the MESH label for the given MESH ID.

    Uses the mappings table in `indra/resources`; if the MESH ID is not listed
    there, falls back on the NLM REST API.

    Parameters
    ----------
    mesh_id : str
        MESH Identifier, e.g. 'D003094'.
    offline : bool
        Whether to allow queries to the NLM REST API if the given MESH ID is
        not contained in INDRA's internal MESH mappings file. Default is False
        (allows REST API queries).

    Returns
    -------
    str
        Label for the MESH ID, or None if the query failed or no label was
        found.
    """
    indra_mesh_mapping = mesh_id_to_name.get(mesh_id)
    if offline or indra_mesh_mapping is not None:
        return indra_mesh_mapping
    # Look up the MESH mapping from NLM if we don't have it locally

```
