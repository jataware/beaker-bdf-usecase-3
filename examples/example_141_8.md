# Description
Example of fetching the post-translational modifications for a given protein ID using the Uniprot client.

# Code
```
indra.databases import uniprot_client
indra.util import unicode_strs

@pytest.mark.webservice
def test_get_modifications():
    mods = uniprot_client.get_modifications('P27361')
    assert ('Phosphothreonine', 202) in mods
    assert ('Phosphotyrosine', 204) in mods

```
