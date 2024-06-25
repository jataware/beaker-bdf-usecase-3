# Description
Get primary ID corresponding to an alternative/deprecated GO ID.

# Code
```
import logging
from indra.databases.obo_client import OboClient

logger = logging.getLogger(__name__)

def get_primary_id(go_id):
    """Get primary ID corresponding to an alternative/deprecated GO ID.

    Parameters
    ----------
    go_id : str
        The GO ID to get the primary ID for.

    Returns
    -------
    str
        Primary identifier corresponding to the given ID.
    """

```
