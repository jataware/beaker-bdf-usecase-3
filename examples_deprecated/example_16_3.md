# Description
Get ID corresponding to a given GO label or synonym.

# Code
```
import logging
from indra.databases.obo_client import OboClient

logger = logging.getLogger(__name__)

def get_go_id_from_label_or_synonym(label):
    """Get ID corresponding to a given GO label or synonym

    Parameters
    ----------
    label : str
        The GO label or synonym to get the ID for.

    Returns
    -------
    str
        Identifier corresponding to the GO label or synonym, starts with GO:.
    """

```
