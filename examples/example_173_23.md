# Description
Add nodes for ChEMBL entities.

# Code
```

def add_chembl_nodes(self):
    from indra.databases import chembl_client
    nodes = []
    for chembl_id, chembl_name in chembl_client.chembl_names.items():
        nodes.append((self.label('CHEMBL', chembl_id),
                      {'name': chembl_name}))

```
