# Description
Add cross-references (xrefs) for PubChem.

# Code
```

def add_pubchem_xrefs(self):
    from indra.databases import pubchem_client
    edges = []
    for pubchem_id, mesh_id in pubchem_client.pubchem_mesh_map.items():
        edges.append((self.label('PUBCHEM', pubchem_id),
                      self.label('MESH', mesh_id),
                      {'type': 'xref', 'source': 'pubchem'}))

```
