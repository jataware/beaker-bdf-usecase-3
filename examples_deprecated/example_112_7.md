# Description
Example of standardizing database references between varied identifiers like EFO, HP, DOID, and MESH.

# Code
```

def test_standardize_db_refs_efo_hp_doid():
    refs = standardize_db_refs({'EFO': '0009502'})
    assert refs.get('MESH') == 'D000007', refs
    refs = standardize_db_refs({'MESH': 'D000007'})
    assert refs.get('EFO') == '0009502', refs

    refs = standardize_db_refs({'HP': 'HP:0031801'})
    assert refs.get('MESH') == 'D064706', refs
    refs = standardize_db_refs({'MESH': 'D064706'})
    assert refs.get('HP') == 'HP:0031801', refs

    # Currently there is no one-to-many mapping in the direction towards MeSH
    # (there used to be) if there is again, we should test it here
    #refs = standardize_db_refs({'DOID': 'DOID:0060695'})
    #assert 'MESH' not in refs

    # One-to-many mappings away from MESH
    refs = standardize_db_refs({'MESH': 'D000071017'})
    assert 'DOID' not in refs

    refs = standardize_db_refs({'DOID': 'DOID:0060495'})
    assert refs.get('MESH') == 'D000067208'

    # This is an xrefs-based mapping that isn't in Gilda's resource file
    refs = standardize_db_refs({'EFO': '0000694'})

```
