# Description
Add MeSH term cross-references (xrefs) to other databases.

# Code
```

def add_mesh_xrefs(self):
    from indra.databases import mesh_client
    edges = []
    data = {'type': 'xref', 'source': 'gilda'}
    for mesh_id, (db_ns, db_id) in mesh_client.mesh_to_db.items():
        edges.append((self.label('MESH', mesh_id),
                      self.label(db_ns, db_id),
                      data))
    for (db_ns, db_id), mesh_id in mesh_client.db_to_mesh.items():
        # There are a variety of namespaces that are being mapped to MeSH
        # here but we specifically avoid UP and HGNC mappings since
        # they can lead to inconsistencies in this direction due to
        # gene vs protein and species-specificity issues.
        if db_ns in {'UP', 'HGNC'}:
            continue
        edges.append((self.label(db_ns, db_id),
                      self.label('MESH', mesh_id),
                      data))

```
