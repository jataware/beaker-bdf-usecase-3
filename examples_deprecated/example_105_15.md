# Description
Example of mapping MESH ID from another database ID and vice versa using `mesh_client.get_mesh_id_from_db_id` and `mesh_client.get_db_mapping`.

# Code
```

def test_mesh_mapping():
    assert mesh_client.get_mesh_id_from_db_id('CHEBI', 'CHEBI:90943') == \
        'C000596361'
    assert mesh_client.get_db_mapping('C000596361') == \

```
