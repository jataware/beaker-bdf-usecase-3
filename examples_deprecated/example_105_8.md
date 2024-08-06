# Description
Example of handling a missing MESH term locally using `mesh_client.get_mesh_id_name` in offline mode.

# Code
```

def test_mesh_term_local_missing():
    mesh_term = 'XXXX'  # dummy term to make sure we don't have it offline
    mesh_id, mesh_name = mesh_client.get_mesh_id_name(mesh_term, offline=True)
    assert mesh_id is None

```
