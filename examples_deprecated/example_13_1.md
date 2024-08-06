# Description
Retrieve the name corresponding to a given Disease Ontology (DOID) identifier.

# Code
```
from indra.databases.obo_client import OboClient


def get_doid_name_from_doid_id(doid_id):
    """Return the name corresponding to the given Disease Ontology ID.

    Parameters
    ----------
    doid_id : str
        The Disease Ontology identifier to be converted.
        Example: "DOID:0000017"

    Returns
    -------
    doid_name : str
        The DOID name corresponding to the given DOID identifier.
    """

```
