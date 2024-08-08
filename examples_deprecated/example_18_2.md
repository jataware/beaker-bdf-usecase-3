# Description
Retrieve IDO identifier from an IDO name using OwlClient.

# Code
```
typing import Optional
indra.databases.owl_client import OwlClient

def get_ido_id_from_ido_name(ido_name: str) -> Optional[str]:
    """Return the HP identifier corresponding to the given IDO name.

    Parameters
    ----------
    ido_name :
        The IDO name to be converted. Example: "parasite role"

    Returns
    -------
    :
        The IDO identifier corresponding to the given IDO name.
    """

```
