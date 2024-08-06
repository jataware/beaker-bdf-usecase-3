# Description
Get ID corresponding to a given GO label.

# Code
```
import logging
from indra.databases.obo_client import OboClient

logger = logging.getLogger(__name__)

def get_go_id_from_label(label):
    """Get ID corresponding to a given GO label.

    Parameters
    ----------
    label : str
        The GO label to get the ID for.

    Returns
    -------
    str
        Identifier corresponding to the GO label, starts with GO:.
    """

```
