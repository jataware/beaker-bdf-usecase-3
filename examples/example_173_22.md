# Description
Add cross-references (xrefs) for miRBase.

# Code
```

def add_mirbase_xrefs(self):
    from indra.databases import mirbase_client
    edges = []
    for mirbase_id, hgnc_id in \
            mirbase_client._mirbase_id_to_hgnc_id.items():
        edges.append((self.label('MIRBASE', mirbase_id),
                      self.label('HGNC', hgnc_id),
                      {'type': 'xref', 'source': 'mirbase'}))
    for hgnc_id, mirbase_id in \
            mirbase_client._hgnc_id_to_mirbase_id.items():
        edges.append((self.label('HGNC', hgnc_id),
                      self.label('MIRBASE', mirbase_id),
                      {'type': 'xref', 'source': 'mirbase'}))

```
