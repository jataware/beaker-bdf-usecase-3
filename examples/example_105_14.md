# Description
Example of checking MESH tree prefixes to determine types using `mesh_client.is_disease`, `mesh_client.is_enzyme`, `mesh_client.is_molecular`, `mesh_client.is_protein`.

# Code
```

def test_tree_prefixes():
    assert mesh_client.is_disease('D009369')
    assert mesh_client.is_enzyme('D005979')
    assert mesh_client.is_molecular('D000077484')

```
