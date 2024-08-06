# Description
Plot a given subgraph from the ontology using NetworkX and Matplotlib.

# Code
```
collections import Counter, defaultdict
networkx
indra.ontology.bio import bio_ontology

def plot_problem(problem):
    import matplotlib.pyplot as plt
    plt.ion()
    plt.figure()
    G = bio_ontology.subgraph(problem)
    pos = networkx.spring_layout(G)
    networkx.draw_networkx(G, pos, node_color='pink')
    edge_labels = networkx.get_edge_attributes(G, 'source')
    networkx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

```
