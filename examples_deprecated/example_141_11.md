# Description
Example of fetching the function description of a protein using the Uniprot client.

# Code
```
from indra.databases import uniprot_client

@pytest.mark.webservice
def test_get_function():
    fun = uniprot_client.get_function('P15056')

```
