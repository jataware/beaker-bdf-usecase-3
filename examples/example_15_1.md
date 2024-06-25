# Description
Retrieve the EFO name corresponding to a given EFO ID.

# Code
```
from indra.databases.obo_client import OboClient


def get_efo_name_from_efo_id(efo_id):
    """Return the EFO name corresponding to the given EFO ID.

    Parameters
    ----------
    efo_id : str
        The EFO identifier to be converted. Example: "0005557"

    Returns
    -------
    efo_name : str
        The EFO name corresponding to the given EFO identifier.
    """

```
