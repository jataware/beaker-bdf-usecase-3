# Description
This example demonstrates how to perform various lookups using the `mgi_client` from the `indra.databases` library. The lookups include fetching an ID from a name, fetching a name from an ID, and working with synonyms.

# Code
```

def test_lookups():
    assert mgi_client.get_id_from_name('Braf') == '88190'
    assert mgi_client.get_name_from_id('1926283') == 'Pgap6'
    assert mgi_client.get_id_from_name_synonym('Pgap6') == '1926283'
    assert mgi_client.get_id_from_name_synonym('Tmem8') == '1926283'
    assert isinstance(mgi_client.get_id_from_name_synonym('EGF-TM7'), list)

```
