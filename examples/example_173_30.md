# Description
Add modification hierarchy within the ontology.

# Code
```

def add_modification_hierarchy(self):
    self.add_edges_from([
        (self.label('INDRA_MODS', source),
         self.label('INDRA_MODS', 'modification'),
         {'type': 'isa'})
        for source in modtype_conditions
        if source != 'modification'
        ]

```
