# Description
Example of applying an edge filter in breadth-first search (BFS) using the `bfs_search` function. Demonstrates filtering edges based on a belief value.

# Code
```
import networkx as nx
from collections import deque
import sys
from copy import deepcopy
import logging

logger = logging.getLogger(__name__)


def get_sorted_neighbors(G, node, reverse, force_edges, edge_filter):
    # Mock implementation of get_sorted_neighbors function for completeness
    # In actual usage, replace this with the correct implementation.
    return G.successors(node) if not reverse else G.predecessors(node)

class Node:
    pass

class Edge:
    pass

class EdgeFilter:
    pass

class SendType:

g = nx.DiGraph({'CHEK1': {'FANC': {'belief': 1}}})
def filter_example(g, u, v):
   return g.edges[u, v].get('belief', 0) > 0.75
path_generator = bfs_search(g, source_node='CHEK1',

```
