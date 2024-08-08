# Description
Example of MESH term name normalization testing both offline and online modes using `mesh_client.get_mesh_id_name`.

# Code
```

def test_mesh_term_name_norm():
    # For this one, the corresponding descriptor is D016922, which is in the
    # INDRA resource file; however, the descriptor name is "Cellular
    # Senescence".  This test verifies the expected behavior that in
    # offline-only mode, "Cellular Senescence" will return the correct
    # descriptor ID, but "Cell Aging" will not, unless using the REST service.
    query_name = 'Cellular Senescence'
    mesh_id, mesh_name = mesh_client.get_mesh_id_name(query_name, offline=True)
    assert mesh_id == 'D016922'
    assert mesh_name == query_name
    query_name = 'Cell Aging'
    mesh_id, mesh_name = mesh_client.get_mesh_id_name(query_name, offline=True)
    assert mesh_id is None
    assert mesh_name is None
    mesh_id, mesh_name = mesh_client.get_mesh_id_name(query_name, offline=False)
    assert mesh_id == 'D016922'

```
