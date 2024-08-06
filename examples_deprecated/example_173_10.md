# Description
Add replacements from OBO data sources.

# Code
```

def add_obo_replacements(self):
    from indra.databases import obo_client
    edges = []
    for ns in self.ontology_namespaces:
        oc = obo_client.OntologyClient(prefix=ns)
        for alt_id, prim_id in oc.alt_to_id.items():
            if alt_id.startswith(ns.upper()) and \
                    prim_id.startswith(ns.upper()):
                edges.append((self.label(ns.upper(), alt_id),
                             self.label(ns.upper(), prim_id),
                             {'type': 'replaced_by'}))

```
