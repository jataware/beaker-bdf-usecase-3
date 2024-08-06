# Description
Test examples for the `get_bioregistry_curie` function, showing how to generate a CURIE based on bioregistry namespace and identifier.

# Code
```

def test_get_bioregistry_curie():
    assert bioregistry_client.get_bioregistry_curie('PUBCHEM', '100101') == \
        'pubchem.compound:100101'
    assert bioregistry_client.get_bioregistry_curie('NXPFA', '01405') == \
        'nextprot.family:01405'
    assert bioregistry_client.get_bioregistry_curie('HGNC', '1097') == \
        'hgnc:1097'
    assert bioregistry_client.get_bioregistry_curie('CVCL', 'CVCL_1234') == \

```
