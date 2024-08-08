# Description
Example of querying a protein by its ID using the Uniprot client and checking if it exists.

# Code
```
from indra.databases import uniprot_client

@pytest.mark.webservice
def test_query_protein_exists():
    g = uniprot_client.query_protein('P00533')

```
