# Description
Example of MESH term lookup locally using `mesh_client.get_mesh_id_name` in offline mode.

# Code
```

def test_mesh_term_lookup_local():
    mesh_term = 'Glucosylceramides'
    (mesh_id, mesh_name) = mesh_client.get_mesh_id_name(mesh_term, offline=True)
    assert mesh_id == 'D005963'

```
