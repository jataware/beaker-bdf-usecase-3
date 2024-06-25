# Description
Example of checking MESH hierarchical relationships using `mesh_client.mesh_isa` and `mesh_client.mesh_isa_web`.

# Code
```

def test_mesh_isa():
    assert mesh_client.mesh_isa('D011506', 'D000602')
    assert not mesh_client.mesh_isa('D000602', 'D011506')

```
