# Description
Get the MONDO identifier corresponding to a given MONDO alt id.

# Code
```
from indra.databases.obo_client import OboClient

def get_id_from_alt_id(mondo_alt_id: str) -> Optional[str]:
    """Return the identifier corresponding to the given MONDO alt id.

    Parameters
    ----------
    mondo_alt_id :
        The MONDO alt id to be converted. Example: "0024812"

    Returns
    -------
    :
        The MONDO identifier corresponding to the given alt id.

    >>> from indra.databases import mondo_client
    >>> mondo_client.get_id_from_alt_id('0018220')
    '0002413'
    """

```
