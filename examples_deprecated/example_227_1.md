# Description
Test IDO name and identifier lookup using the indra.databases.ido_client

# Code
```

def test_lookup():
    """Test IDO name and identifier lookup."""
    name = ido_client.get_ido_name_from_ido_id("0000403")
    assert "parasite role" == name, name

    identifier = ido_client.get_ido_id_from_ido_name("parasite role")

```
