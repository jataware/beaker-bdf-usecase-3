# Description
Use the `get_mesh_id` method from the Pubchem client to obtain MeSH IDs for given PubChem compound IDs, with error handling for invalid IDs.

# Code
```

def test_mesh_mappings():
    mesh_id = pubchem_client.get_mesh_id('56649450')  # Alpelisib
    assert mesh_id == 'C585539', mesh_id

```
