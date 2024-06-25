# Description
Add nodes for DrugBank entities.

# Code
```

def add_drugbank_nodes(self):
    from indra.databases import drugbank_client
    nodes = []
    for db_id, db_name in drugbank_client.drugbank_names.items():
        nodes.append((self.label('DRUGBANK', db_id),
                      {'name': db_name}))

```
