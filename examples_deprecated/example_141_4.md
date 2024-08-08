# Description
Example of fetching family members of a protein using the Uniprot client.

# Code
```
indra.databases import uniprot_client
indra.util import unicode_strs

@pytest.mark.webservice
def test_get_family_members():
    members = uniprot_client.get_family_members('RAF')
    assert 'ARAF' in members
    assert 'BRAF' in members
    assert 'RAF1' in members

```
