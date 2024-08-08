# Description
Print details of a cycle found in the ontology, illustrating hierarchical relationships.

# Code
```
from indra.ontology.bio import bio_ontology

def print_cycle(cycle):
    for n1, n2 in zip(cycle, cycle[1:] + cycle[:1]):
        print('%s (%s)-[%s]-%s (%s)' % (
            bio_ontology.get_name(*bio_ontology.get_ns_id(n1)), n1,
            bio_ontology.edges[n1, n2]['type'],
            bio_ontology.get_name(*bio_ontology.get_ns_id(n2)), n2
            )

```
