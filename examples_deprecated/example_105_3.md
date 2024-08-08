# Description
Example of MESH ID lookup locally using `mesh_client.get_mesh_name` in offline mode.

# Code
```

def test_mesh_id_lookup_local():
    mesh_id = 'D005963'
    mesh_name = mesh_client.get_mesh_name(mesh_id, offline=True)

```
