# Description
Example of checking supplementary MESH ID lookup locally using `mesh_client.get_mesh_name` in offline mode.

# Code
```

def test_mesh_supplementary_id_lookup_local():
    mesh_id = 'C056331'
    mesh_name = mesh_client.get_mesh_name(mesh_id, offline=True)

```
