# Description
Example of validating and mapping supplementary MESH IDs to primary IDs using `mesh_client.mesh_supp_to_primary` and `mesh_client.get_primary_mappings`.

# Code
```
from indra.databases import mesh_client

def test_supplementary_to_primary():
    from indra.statements.validate import assert_valid_id
    for supp, primaries in mesh_client.mesh_supp_to_primary.items():
        for primary in primaries:
            assert_valid_id('MESH', primary)
    mesh_client.get_primary_mappings('C009879') == ['D011140']

```
