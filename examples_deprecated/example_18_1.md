# Description
Retrieve IDO name from an IDO identifier using OwlClient.

# Code
```
typing import Optional
indra.databases.owl_client import OwlClient

def get_ido_name_from_ido_id(ido_id: str) -> Optional[str]:
    """Return the HP name corresponding to the given HP ID.

    Parameters
    ----------
    ido_id :
        The IDO identifier to be converted. Example: "0000403"

    Returns
    -------
    :
        The IDO name corresponding to the given IDO identifier.
    """

```
