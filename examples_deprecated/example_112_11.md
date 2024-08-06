# Description
Example of standardizing database references using DRUGBANK identifier and checking CHEBI and CHEMBL mappings.

# Code
```

def test_drugbank_mappings():
    name, db_refs = standardize_name_db_refs({'DRUGBANK': 'DB00001'})
    assert db_refs.get('CHEBI') == 'CHEBI:142437', db_refs
    assert db_refs.get('CHEMBL') == 'CHEMBL1201666', db_refs
    assert name == 'lepirudin'
    # Here we test for alternative prioritization of name spaces
    name, db_refs = standardize_name_db_refs({'DRUGBANK': 'DB00001'},
                                             ns_order=['DRUGBANK', 'CHEBI'])
    # We expect to get the Drugbank standard name

```
