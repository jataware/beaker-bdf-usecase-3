# Description
This example demonstrates how to convert an HP ID to its corresponding HP name using the `OboClient` from the `indra.databases.obo_client` library.

# Code
```
from indra.databases.obo_client import OboClient


def get_hp_name_from_hp_id(hp_id):
    """Return the HP name corresponding to the given HP ID.

    Parameters
    ----------
    hp_id : str
        The HP identifier to be converted. Example: "HP:0000017"

    Returns
    -------
    hp_name : str
        The HP name corresponding to the given HP identifier.
    """

```
