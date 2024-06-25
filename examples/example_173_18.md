# Description
Add cross-references (xrefs) for NCIT terms.

# Code
```

def add_ncit_xrefs(self):
    from indra.sources.trips.processor import ncit_map
    edges = []
    for ncit_id, (target_ns, target_id) in ncit_map.items():
        edges.append((self.label('NCIT', ncit_id),
                      self.label(target_ns, target_id),
                      {'type': 'xref', 'source': 'ncit'}))

```
