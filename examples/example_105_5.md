# Description
Example of handling a missing MESH ID locally using `mesh_client.get_mesh_name` in offline mode.

# Code
```

def test_mesh_id_local_missing():
    mesh_id = 'XXXX'  # dummy name to make sure we don't have it offline
    mesh_name = mesh_client.get_mesh_name(mesh_id, offline=True)

```
