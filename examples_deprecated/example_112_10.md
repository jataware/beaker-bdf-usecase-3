# Description
Example of standardizing a microRNA name and database references using HGNC and MIRBASE identifiers.

# Code
```

def test_mirna_standardize():
    name, db_refs = standardize_name_db_refs({'HGNC': '31476'})
    assert db_refs['HGNC'] == '31476'
    assert db_refs['MIRBASE'] == 'MI0000060'
    assert name == 'MIRLET7A1'

    name, db_refs = standardize_name_db_refs({'MIRBASE': 'MI0001730'})
    assert db_refs['MIRBASE'] == 'MI0001730'

```
