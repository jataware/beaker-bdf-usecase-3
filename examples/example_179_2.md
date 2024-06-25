# Description
Process a BioFactoid document using a given JSON object.

# Code
```
import requests
from .processor import BioFactoidProcessor

biofactoid_url = 'https://biofactoid.org/api/document'
biofactoid_unstable_url = 'https://unstable.factoid.baderlab.org/api/document'


def process_json(biofactoid_json):
    """Process BioFactoid JSON.

    Parameters
    ----------
    biofactoid_json : json
        The BioFactoid JSON object to process.

    Returns
    -------
    BioFactoidProcessor
        A processor which contains extracted INDRA Statements in its
        statements attribute.
    """
    bp = BioFactoidProcessor(biofactoid_json)
    bp.extract_statements()

```
