# Description
Test conversion from HGNC ID to miRBase ID.

# Code
```

def test_hgnc_mirbase_mappings():
    assert 'MI0000060' == mirbase_client.get_mirbase_id_from_hgnc_id('31476')
    assert mirbase_client.get_mirbase_id_from_hgnc_id('6893') is None, \

```
