# Description
Add nodes based on MeSH terms.

# Code
```

def add_mesh_nodes(self):
    from indra.databases import mesh_client
    nodes = [(self.label('MESH', mesh_id),
              {'name': name,
               'type': _get_mesh_type(mesh_client, mesh_id)})
             for mesh_id, name in
             mesh_client.mesh_id_to_name.items()]

```
