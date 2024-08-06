# Description
Test examples for the `get_bioregistry_url` function, demonstrating how to generate specific URLs using bioregistry namespace and identifier.

# Code
```

def test_get_bioregistry_url():
    assert bioregistry_client.get_bioregistry_url('PUBCHEM', '100101') == \
        'https://bioregistry.io/pubchem.compound:100101'
    assert bioregistry_client.get_bioregistry_url('CVCL', 'CVCL_0440') == \

```
