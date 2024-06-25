# Description
Test examples for the `ensure_prefix_if_needed` function, showing how to ensure that identifiers either have or do not duplicate a prefix.

# Code
```

def test_ensure_prefix_if_needed():
    assert bioregistry_client.ensure_prefix_if_needed('PUBCHEM', '100101') == \
        '100101'
    assert bioregistry_client.ensure_prefix_if_needed('CHEBI', '3696') == \
        'CHEBI:3696'
    assert bioregistry_client.ensure_prefix_if_needed('CHEBI', 'CHEBI:3696') == \
        'CHEBI:3696'
    assert bioregistry_client.ensure_prefix_if_needed('CVCL', '0440') == \

```
