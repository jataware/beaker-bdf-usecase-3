# Description
Example of mapping MESH IDs to GO IDs and vice versa using `mesh_client.get_go_id` and `mesh_client.get_mesh_id_from_go_id`.

# Code
```

def test_mesh_go_mappings():
    assert mesh_client.get_go_id('D059765') == 'GO:0035825'

```
