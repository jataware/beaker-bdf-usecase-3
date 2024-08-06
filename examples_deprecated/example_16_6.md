# Description
Return the GO namespace associated with a GO ID.

# Code
```
import logging
from typing import Union
from indra.databases.obo_client import OboClient

logger = logging.getLogger(__name__)

def get_namespace(go_id: str) -> Union[str, None]:
    """Return the GO namespace associated with a GO ID.

    Parameters
    ----------
    go_id :
        The GO ID to get the namespace for

    Returns
    -------
    :
        The GO namespace for the given ID. This is one of
        molecular_function, biological_process or cellular_component.
        If the GO ID is not available as an entry, None is returned.
    """

```
