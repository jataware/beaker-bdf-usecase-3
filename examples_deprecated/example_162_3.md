# Description
Flattening the IndraNet into a signed graph. This example demonstrates how to convert an IndraNet to a signed graph using a given mapping of statement types to signs, and optionally using a flattening method and weight mapping function.

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
def default_flattening_function(G, edge):
    all_beliefs = [s['belief'] for s in G.edges[edge]['statements']]
    return sum(all_beliefs)/len(all_beliefs)

    def to_signed_graph(self, sign_dict=None,
                        flattening_method=None, weight_mapping=None):
        """Flatten the IndraNet to a signed graph.

        Parameters
        ----------
        sign_dict : dict
            A dictionary mapping a Statement type to a sign to be used for
            the edge. By default only Activation and IncreaseAmount are added
            as positive edges and Inhibition and DecreaseAmount are added as
            negative edges, but a user can pass any other Statement types in
            a dictionary.
        flattening_method : str or function(networkx.DiGraph, edge)
            The method to use when updating the belief for the flattened edge.

            If a string is provided, it must be one of the predefined options
            'simple_scorer' or 'complementary_belief'.

            If a function is provided, it must take the flattened graph 'G'
            and an edge 'edge' to perform the belief flattening on and return
            a number:

            >>> def flattening_function(G, edge):
            ...     # Return the average belief score of the constituent edges
            ...     all_beliefs = [s['belief']
            ...         for s in G.edges[edge]['statements']]
            ...     return sum(all_beliefs)/len(all_beliefs)

        weight_mapping : function(networkx.DiGraph)
            A function taking at least the graph G as an argument and
            returning G after adding edge weights as an edge attribute to the
            flattened edges using the reserved keyword 'weight'.

            Example:

            >>> def weight_mapping(G):
            ...     # Sets the flattened weight to the average of the
            ...     # inverse source count
            ...     for edge in G.edges:
            ...         w = [1/s['evidence_count']
            ...             for s in G.edges[edge]['statements']]
            ...         G.edges[edge]['weight'] = sum(w)/len(w)
            ...     return G

        Returns
        -------
        SG : IndraNet(nx.MultiDiGraph)
            An IndraNet graph flattened to a signed graph
        """
        sign_dict = default_sign_dict if not sign_dict else sign_dict

        SG = nx.MultiDiGraph()
        for u, v, data in self.edges(data=True):
            # Add nodes and their attributes
            if u not in SG.nodes:
                SG.add_node(u, **self.nodes[u])
            if v not in SG.nodes:
                SG.add_node(v, **self.nodes[v])
            # Explicit 'is not None' needed to accept 0
            if data.get('initial_sign') is not None:
                sign = data['initial_sign']
            elif data['stmt_type'] not in sign_dict:
                continue
            else:
                sign = sign_dict[data['stmt_type']]
            if SG.has_edge(u, v, sign):
                SG[u][v][sign]['statements'].append(data)
            else:
                SG.add_edge(u, v, sign, statements=[data], sign=sign)
        SG = self._update_edge_belief(SG, flattening_method)
        if weight_mapping:
            SG = weight_mapping(SG)

```
