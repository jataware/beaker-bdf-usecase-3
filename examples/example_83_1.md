# Description
Fix database references in a dictionary using the `fix_invalidities_db_refs` function.

# Code
```

def test_fix_db_refs():
    assert fix_invalidities_db_refs({'CHEBI': '123'}) == \
           {'CHEBI': 'CHEBI:123'}
    assert fix_invalidities_db_refs({'CHEMBL': '123'}) == \
           {'CHEMBL': 'CHEMBL123'}
    assert fix_invalidities_db_refs({'PUBCHEM': 'CID: 123'}) == \
           {'PUBCHEM': '123'}
    assert fix_invalidities_db_refs({'ECCODE': '1.2.-.-'}) == \
           {'ECCODE': '1.2'}
    assert fix_invalidities_db_refs({'UNIPROT': 'P12345'}) == \
           {'UP': 'P12345'}
    assert fix_invalidities_db_refs({'UNIPROT': 'SL-123'}) == \
           {'UPLOC': 'SL-123'}
    assert fix_invalidities_db_refs({'MGI': 'Mgi:Abcd1'}) == \
           {}
    assert fix_invalidities_db_refs({'RGD': 'Abcd1'}) == \

```
