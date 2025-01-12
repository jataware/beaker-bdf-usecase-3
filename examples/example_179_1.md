# Description
Process a BioFactoid document from the web using the default or specified URL.

# Code
```
import requests
from .processor import BioFactoidProcessor

biofactoid_url = 'https://biofactoid.org/api/document'
biofactoid_unstable_url = 'https://unstable.factoid.baderlab.org/api/document'


def process_from_web(url=None):
    """Process BioFactoid documents from the web.

    Parameters
    ----------
    url : Optional[str]
        The URL for the web service endpoint which contains all the
        document data.

    Returns
    -------
    BioFactoidProcessor
        A processor which contains extracted INDRA Statements in its
        statements attribute.
    """
    url = url if url else biofactoid_url
    res = requests.get(url)
    res.raise_for_status()

```
