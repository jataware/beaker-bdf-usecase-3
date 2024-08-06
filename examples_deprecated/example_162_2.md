# Description
Flattening the IndraNet to a directed (DiGraph) graph. This method showcases how to convert an IndraNet into a simpler DiGraph structure, optionally applying a flattening method and a weight mapping function.

# Code
```
import pandas as pd
import networkx as nx
from indra.statements import Evidence, Statement
from indra.belief import SimpleScorer
def default_weight_mapping(G):
    for edge in G.edges:
        w = [1/s['evidence_count'] for s in G.edges[edge]['statements']]
        G.edges[edge]['weight'] = sum(w)/len(w)
    return G

    def to_digraph(self, flattening_method=None, weight_mapping=None):
        """Flatten the IndraNet to a DiGraph

        Parameters
        ----------
        flattening_method : str|function
            The method to use when updating the belief for the flattened edge
        weight_mapping : function
            A function taking at least the graph G as an argument and
            returning G after adding edge weights as an edge attribute to the
            flattened edges using the reserved keyword 'weight'.

        Returns
        -------
        G : IndraNet(nx.DiGraph)
            An IndraNet graph flattened to a DiGraph
        """
        G = nx.DiGraph()
        for u, v, data in self.edges(data=True):
            # Add nodes and their attributes
            if u not in G.nodes:
                G.add_node(u, **self.nodes[u])
            if v not in G.nodes:
                G.add_node(v, **self.nodes[v])
            # Add edges and their attributes
            if G.has_edge(u, v):
                G[u][v]['statements'].append(data)
            else:
                G.add_edge(u, v, statements=[data])
        G = self._update_edge_belief(G, flattening_method)
        if weight_mapping:
            G = weight_mapping(G)

```
