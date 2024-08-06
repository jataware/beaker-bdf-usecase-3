# Description
Example of MESH ID fallback to REST service using `mesh_client.get_mesh_name` in online mode.

# Code
```

def test_mesh_id_fallback_to_rest():
    mesh_id = 'D015242'
    mesh_name = mesh_client.get_mesh_name(mesh_id, offline=False)

```
