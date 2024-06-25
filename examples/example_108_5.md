# Description
Test conversion from HGNC symbol to miRBase ID.

# Code
```

def test_hgnc_symbol_mirbase_mappings():
    assert 'MI0000075' == \
                    mirbase_client.get_mirbase_id_from_hgnc_symbol('MIR19B2')
    assert mirbase_client.get_mirbase_id_from_hgnc_symbol('MAPT') is None, \

```
