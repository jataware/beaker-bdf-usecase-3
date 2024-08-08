# Description
Add activity hierarchy within the ontology.

# Code
```

def add_activity_hierarchy(self):
    rels = [
        ('transcription', 'activity'),
        ('catalytic', 'activity'),
        ('gtpbound', 'activity'),
        ('kinase', 'catalytic'),
        ('phosphatase', 'catalytic'),
        ('gef', 'catalytic'),
        ('gap', 'catalytic')
    ]
    self.add_edges_from([
        (self.label('INDRA_ACTIVITIES', source),
         self.label('INDRA_ACTIVITIES', target),
         {'type': 'isa'})
        for source, target in rels
        ]

```
