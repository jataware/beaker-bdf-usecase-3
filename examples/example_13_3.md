# Description
Retrieve the identifier corresponding to a given Disease Ontology alternate identifier.

# Code
```
from indra.databases.obo_client import OboClient


def get_doid_id_from_doid_alt_id(doid_alt_id):
    """Return the identifier corresponding to the given Disease Ontology alt id.

    Parameters
    ----------
    doid_alt_id : str
        The Disease Ontology alt id to be converted. Example: "DOID:267"

    Returns
    -------
    doid_id : str
        The Disease Ontology identifier corresponding to the given alt id.
    """

```
