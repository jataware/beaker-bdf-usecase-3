# Description
Retrieve the EFO identifier corresponding to a given EFO name.

# Code
```
from indra.databases.obo_client import OboClient


def get_efo_id_from_efo_name(efo_name):
    """Return the EFO identifier corresponding to the given EFO name.

    Parameters
    ----------
    efo_name : str
        The EFO name to be converted. Example: "gum cancer"

    Returns
    -------
    efo_id : str
        The EFO identifier corresponding to the given EFO name.
    """

```
