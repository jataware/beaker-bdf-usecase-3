# Description
Return the MeSH ID for a given PubChem CID.

# Code
```
from typing import Union


def get_mesh_id(pubchem_cid: str) -> Union[str, None]:
    """Return the MeSH ID for a given PubChem CID.

    Parameters
    ----------
    pubchem_cid :
        The PubChem CID whose MeSH ID should be returned.

    Returns
    -------
    :
        The MeSH ID corresponding to the PubChem CID or None
        if not available.
    """

```
