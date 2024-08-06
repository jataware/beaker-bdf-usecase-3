# Description
Add hierarchies for MeSH terms.

# Code
```

def add_mesh_hierarchy(self):
    from indra.databases import mesh_client
    mesh_tree_numbers_to_id = {}
    for mesh_id, tns in mesh_client.mesh_id_to_tree_numbers.items():
        for tn in tns:
            mesh_tree_numbers_to_id[tn] = mesh_id
    edges = []
    for mesh_id, tns in mesh_client.mesh_id_to_tree_numbers.items():
        parents_added = set()
        for tn in tns:
            if '.' not in tn:
                continue
            parent_tn, _ = tn.rsplit('.', maxsplit=1)
            parent_id = mesh_tree_numbers_to_id[parent_tn]
            if parent_id in parents_added:
                continue
            edges.append((self.label('MESH', mesh_id),
                          self.label('MESH', parent_id),
                          {'type': 'isa'}))
    # Handle any replacements
    replacements = [('C000657245', 'D000086382')]
    for mesh_id, replacement_id in replacements:
        edges.append((self.label('MESH', mesh_id),
                      self.label('MESH', replacement_id),

```
