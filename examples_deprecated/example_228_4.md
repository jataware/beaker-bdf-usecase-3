# Description
Test converting secondary MONDO ID to primary MONDO ID

# Code
```

def test_mondo_secondary_to_primary():
    identifier = mondo_client.get_id_from_alt_id('0018220')
    assert identifier is not None

```
