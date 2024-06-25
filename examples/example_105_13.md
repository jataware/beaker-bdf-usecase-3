# Description
Example of getting MESH tree numbers using `mesh_client.get_mesh_tree_numbers` and `mesh_client.get_mesh_tree_numbers_from_web`.

# Code
```

def test_get_mesh_tree_numbers():
    tns = mesh_client.get_mesh_tree_numbers('D000025')
    tnsw = mesh_client.get_mesh_tree_numbers_from_web('D000025')
    assert sorted(tns) == sorted(tnsw), tns
    assert tns == ['E04.520.050.050'], tns
    tns = mesh_client.get_mesh_tree_numbers('D000031')
    assert set(tns) == {'C01.674.173', 'C12.050.703.039.256',

```
