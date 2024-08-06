# Description
Retrieve the identifier corresponding to a given Disease Ontology name.

# Code
```
from indra.databases.obo_client import OboClient


def get_doid_id_from_doid_name(doid_name):
    """Return the identifier corresponding to the given Disease Ontology name.

    Parameters
    ----------
    doid_name : str
        The Disease Ontology name to be converted. Example: "Nocturia"

    Returns
    -------
    doid_id : str
        The Disease Ontology identifier corresponding to the given name.
    """

```
