# Description
Add nodes for miRBase.

# Code
```

def add_mirbase_nodes(self):
    from indra.databases import mirbase_client
    nodes = []
    for mirbase_id, name in mirbase_client._mirbase_id_to_name.items():
        nodes.append((self.label('MIRBASE', mirbase_id),
                      {'name': name}))

```
