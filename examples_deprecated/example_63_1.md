# Description
Test examples for the `get_ns_from_bioregistry` function, demonstrating various inputs and expected outputs.

# Code
```

def test_get_ns_from_bioregistry():
    assert bioregistry_client.get_ns_from_bioregistry('xxxx') is None
    assert bioregistry_client.get_ns_from_bioregistry('noncodev4.rna') == \
        'NONCODE'

```
