# Description
Example of fetching the sequence of a protein by its ID using the Uniprot client.

# Code
```
indra.databases import uniprot_client
indra.util import unicode_strs

@pytest.mark.webservice
def test_get_sequence():
    seq = uniprot_client.get_sequence('P00533')
    assert len(seq) > 1000

```
