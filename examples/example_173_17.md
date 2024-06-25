# Description
Add nodes for NCIT terms.

# Code
```

def add_ncit_nodes(self):
    from indra.sources.trips.processor import ncit_map
    nodes = [(self.label('NCIT', ncit_id), {}) for ncit_id in ncit_map]

```
