# Description
Get label corresponding to a given GO identifier.

# Code
```
import logging
from indra.databases.obo_client import OboClient

logger = logging.getLogger(__name__)

def get_go_label(go_id):
    """Get label corresponding to a given GO identifier.

    Parameters
    ----------
    go_id : str
        The GO identifier. Should include the `GO:` prefix, e.g., `GO:1903793`
        (positive regulation of anion transport).

    Returns
    -------
    str
        Label corresponding to the GO ID.
    """

```
