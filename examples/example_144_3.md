# Description
Identify and print strongly connected components (SCCs) in the xref graph and detect cycles in the hierarchy.

# Code
```
from collections import Counter, defaultdict
import networkx
from indra.ontology.bio import bio_ontology


if __name__ == '__main__':
    # First, find strongly connected components in the xref graph where
    # a given namespace appears more than once.
    bio_ontology.initialize()
    xrefs = [(e[0], e[1]) for e in bio_ontology.edges(data=True) if
             e[2]['type'] == 'xref']
    xrefg = bio_ontology.edge_subgraph(xrefs)
    comps = networkx.algorithms.strongly_connected_components(xrefg)

    problems = []
    for comp in comps:
        namespaces = [bio_ontology.get_ns(node) for node in comp]
        cnt = Counter(namespaces)
        if any(v > 1 for k, v in cnt.items()):
            problems.append(comp)

    print('Found %d problems in total' % len(problems))

    problems_by_ns = defaultdict(list)
    for problem in problems:
        nscnt = Counter([bio_ontology.get_ns(n) for n in problem])
        namespaces = [ns for ns, cnt in nscnt.items() if cnt > 1]
        for ns in namespaces:
            problems_by_ns[ns].append(problem)

    for ns, problems_ns in problems_by_ns.items():
        print(ns, len(problems_ns))

    # Next, find cycles in the isa/partof subgraph meaning circular
    # hierarchical relationships.
    hierarchy = [(e[0], e[1]) for e in bio_ontology.edges(data=True) if
                 e[2]['type'] in {'isa', 'partof'}]
    hierarchyg = bio_ontology.edge_subgraph(hierarchy)
    cycles = networkx.simple_cycles(hierarchyg)
    if cycles:
        print('---')
        print('Hierarchical cycles')
        for cycle in cycles:
            print('---')

```
