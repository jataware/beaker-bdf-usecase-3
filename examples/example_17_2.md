# Description
This example demonstrates how to convert an HP name to its corresponding HP ID using the `OboClient` from the `indra.databases.obo_client` library.

# Code
```
from indra.databases.obo_client import OboClient


def get_hp_id_from_hp_name(hp_name):
    """Return the HP identifier corresponding to the given HP name.

    Parameters
    ----------
    hp_name : str
        The HP name to be converted. Example: "Nocturia"

    Returns
    -------
    hp_id : str
        The HP identifier corresponding to the given HP name.
    """

```
