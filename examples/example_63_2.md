# Description
Test examples for the `get_ns_id_from_bioregistry` function, showing how to retrieve namespace and identifier from bioregistry for given prefixes and identifiers.

# Code
```

def test_get_ns_id_from_bioregistry():
    assert bioregistry_client.get_ns_id_from_bioregistry('xxxx', 'xxxx') == \
        (None, None)
    assert bioregistry_client.get_ns_id_from_bioregistry('chebi', '3696') == \
        ('CHEBI', 'CHEBI:3696')
    assert bioregistry_client.get_ns_id_from_bioregistry('hgnc', '1097') == \
        ('HGNC', '1097')
    assert bioregistry_client.get_ns_id_from_bioregistry('cellosaurus',
                                                         '1234') == \

```
