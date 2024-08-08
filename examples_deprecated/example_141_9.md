# Description
Example of verifying the location of a modification site in a protein using the Uniprot client.

# Code
```
from indra.databases import uniprot_client

@pytest.mark.webservice
def test_verify_location():
    assert uniprot_client.verify_location('P27361', 'T', 202)
    assert not uniprot_client.verify_location('P27361', 'S', 202)
    assert not uniprot_client.verify_location('P27361', 'T', -1)

```
