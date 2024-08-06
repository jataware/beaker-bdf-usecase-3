# Description
Example of querying a non-existent protein ID using the Uniprot client.

# Code
```
from indra.databases import uniprot_client

@pytest.mark.webservice
def test_query_protein_nonexist():
    g = uniprot_client.query_protein('XXXX')

```
