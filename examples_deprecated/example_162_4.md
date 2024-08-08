# Description
Updating the belief of edges in the flattened graph using different flattening methods. This static method updates the belief scores of edges in a given networkx graph.

# Code
```
import numpy as np
import logging
import pandas as pd
from decimal import Decimal
from indra.statements import Evidence, Statement
from indra.belief import SimpleScorer
logger = logging.getLogger(__name__)
simple_scorer = SimpleScorer()

    def _update_edge_belief(G, flattening_method):
        """G must be or be a child of an nx.Graph object. If
        'flattening_method' is a function, it must take at least the graph G
        and an edge and return a number (the new belief for the flattened
        edge).

        We assume that G is the flattened graph and that all its edges have an
        edge attribute called 'statements' containing a list of dictionaries
        representing the edge data of all the edges in the un-flattened graph
        that were mapped to the corresponding flattened edge in G.
        """

        if not flattening_method or flattening_method == 'simple_scorer':
            for e in G.edges:
                G.edges[e]['belief'] = _simple_scorer_update(G, edge=e)
        elif flattening_method == 'complementary_belief':
            for e in G.edges:
                G.edges[e]['belief'] = _complementary_belief(G, edge=e)
        else:
            for e in G.edges:
                G.edges[e]['belief'] = flattening_method(G, edge=e)

```
