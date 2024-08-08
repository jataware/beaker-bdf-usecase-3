# Description
Test various lookup functions in the indra.databases.rgd_client library.

# Code
```

def test_lookups():
    assert rgd_client.get_id_from_name('Braf') == '619908'
    assert rgd_client.get_name_from_id('1311395') == 'Pgap6'
    assert rgd_client.get_id_from_name_synonym('Pgap6') == '1311395'
    assert rgd_client.get_id_from_name_synonym('A2maa') == '2004'
    assert isinstance(rgd_client.get_id_from_name_synonym('Cyp2d6'), list)

```
