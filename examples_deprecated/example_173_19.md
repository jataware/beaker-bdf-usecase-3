# Description
Add hierarchies within UniProt fragments.

# Code
```

def add_uppro_hierarchy(self):
    from indra.databases import uniprot_client
    edges = []
    for prot_id, features in uniprot_client.um.features.items():
        prot_node = self.label('UP', prot_id)
        for feature in features:
            if feature.id is None:
                continue
            feat_node = self.label('UPPRO', feature.id)
            edges.append((feat_node, prot_node,
                          {'type': 'partof'}))

```
