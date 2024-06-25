# Description
Add hierarchies from OBO data sources.

# Code
```

    def add_obo_hierarchies(self):
        from indra.databases import obo_client
        edges = []
        # Mapping various source relation types to standardized ones
        # in this ontology graph
        rel_mappings = {
            'xref': 'xref',
            'isa': 'isa',
            'partof': 'partof',
            'is_a': 'isa',
            'part_of': 'partof',
            'has_part': 'partof',
            # These are specifically to map ChEBI relations
            'has_functional_parent': 'isa',
            'has_parent_hydride': 'isa',
            'has_role': 'isa'
        }
        # The source and target for these relations need to be reversed
        # when adding to the graph
        reverse_rel = {
            'has_part',
        }

        exceptions = {
            # Some (non-physical entity) GO terms have a has_part relationship
            # that creates cycles in the isa/partof subgraph. One example is
            # signaling receptor binding (GO:GO:0005102)-[partof]-
            #      pheromone activity (GO:GO:0005186)
            # where the first is actually a more generic term compared to the
            # second. The semantics of these are different from typical partof
            # relations in INDRA so we exclude them.
            'GO': ('has_part', lambda x: x['type'] != 'cellular_component'),
            # Similarly, CHEBI partof/isa relations have cycles, for example,
            # molybdate (CHEBI:CHEBI:36264)-[partof]-
            #     sodium molybdate (anhydrous) (CHEBI:CHEBI:75215)
            # sodium molybdate (anhydrous) (CHEBI:CHEBI:75215)-[partof]-
            #     sodium molybdate tetrahydrate (CHEBI:CHEBI:132099)
            # sodium molybdate tetrahydrate (CHEBI:CHEBI:132099)-[isa]-
            #     molybdate (CHEBI:CHEBI:36264)
            # For simplicity, we exclude all has_part (i.e., reverse partof)
            # relations coming from CHEBI.
            'CHEBI': ('has_part', lambda x: True),
        }

        for ns in self.ontology_namespaces:
            oc = obo_client.OntologyClient(prefix=ns)
            ns_exceptions = exceptions.get(ns.upper())
            for db_id, entry in oc.entries.items():
                for rel, targets in entry.get('relations', {}).items():

                    # Skip unknown relation types
                    mapped_rel = rel_mappings.get(rel)
                    if not mapped_rel:
                        continue
                    if ':' in db_id and not db_id.startswith(ns.upper()):
                        source_label = db_id
                    else:
                        source_label = self.label(ns.upper(), db_id)

                    # Here we check if there is an exception condition defined
                    # on the inclusion of these relations
                    if ns_exceptions and rel == ns_exceptions[0]:
                        if ns_exceptions[1](self.nodes[source_label]):
                            continue

                    for target in targets:
                        if ':' in target and not target.startswith(ns.upper()):
                            target_label = target
                        else:
                            target_label = self.label(ns.upper(), target)
                        if rel in reverse_rel:
                            av = (target_label,
                                  source_label,
                                  {'type': mapped_rel})
                        else:
                            av = (source_label,
                                  target_label,
                                  {'type': mapped_rel})
                        edges.append(av)

```
