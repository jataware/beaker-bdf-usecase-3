# Description
Test examples for the `get_ns_id_from_bioregistry_curie` function, illustrating the retrieval of namespace and identifier from bioregistry using CURIE format.

# Code
```

def test_get_ns_id_from_bioregistry_curie():
    assert bioregistry_client.get_ns_id_from_bioregistry_curie('xxxx:xxxx') == \
        (None, None)
    assert bioregistry_client.get_ns_id_from_bioregistry_curie('chebi:3696') == \
        ('CHEBI', 'CHEBI:3696')
    assert bioregistry_client.get_ns_id_from_bioregistry_curie('hgnc:1097') == \
        ('HGNC', '1097')
    assert bioregistry_client.get_ns_id_from_bioregistry_curie('cellosaurus:0440') == \

```
