# Description
Add nodes from OBO data sources.

# Code
```

def add_obo_nodes(self):
    from indra.databases import obo_client
    nodes = []
    type_functions = {
        'go': _get_go_type,
        'efo': lambda x: 'experimental_factor',
        'hp': lambda x: 'disease',
        'doid': lambda x: 'disease',
        'chebi': lambda x: 'small_molecule',
        'ido': lambda x: 'infectious_disease_concept',
        'mondo': lambda x: 'disease',
        'eccode': lambda x: 'molecular_function',
    }
    for ns in self.ontology_namespaces:
        oc = obo_client.OntologyClient(prefix=ns)
        for db_id, entry in oc.entries.items():
            label = self.label(ns.upper(), db_id)
            # Here we handle and isa relationships that point
            # to an entry outside this ontology. The logic for recognizing
            # these here is: if there is a : in the ID but the prefix is
            # not for this namespace then we assume it's another namespace
            if ':' in db_id and not db_id.startswith(ns.upper()):
                label = db_id
            nodes.append((label,
                          {'name': entry['name'],
                           'type': type_functions[ns](db_id)}))
        # Add nodes for secondary IDs as obsolete
        for alt_id in oc.alt_to_id:
            if alt_id.startswith(ns.upper()):
                nodes.append((self.label(ns.upper(), alt_id),
                              {'obsolete': True}))

```
