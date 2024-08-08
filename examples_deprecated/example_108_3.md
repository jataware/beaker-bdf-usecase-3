# Description
Test conversion from miRBase ID to HGNC ID.

# Code
```

def test_mirbase_hgnc_mappings():
    assert '31476' == mirbase_client.get_hgnc_id_from_mirbase_id('MI0000060')
    assert mirbase_client.get_hgnc_id_from_mirbase_id('MI0000056') is None, \

```
