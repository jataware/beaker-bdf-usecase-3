# Description
Add cross-references (xrefs) from biomappings.

# Code
```

def add_biomappings(self):
    biomappings_tsv = get_resource_path('biomappings.tsv')
    edges = []
    for source_ns, source_id, _, target_ns, target_id, _ in \
            read_unicode_csv(biomappings_tsv, delimiter='\t'):
        edges.append((self.label(source_ns, source_id),
                      self.label(target_ns, target_id),
                      {'type': 'xref', 'source': 'biomappings'}))
        edges.append((self.label(target_ns, target_id),
                      self.label(source_ns, source_id),
                      {'type': 'xref', 'source': 'biomappings'}))

```
