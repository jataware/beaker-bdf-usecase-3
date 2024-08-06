# Description
Test breadth-first search (BFS) algorithm on a signed graph with specific sign constraints.

# Code
```
import numpy as np
import networkx as nx

from indra.explanation.pathfinding.pathfinding import bfs_search
from indra.explanation.pathfinding.util import get_subgraph
from indra.explanation.model_checker.model_checker import signed_edges_to_signed_nodes

INT_PLUS = 0
INT_MINUS = 1


def _digraph_setup():
    # Ensures alphabetical order in reverse traversal
    edge_beliefs = {('Z1', 'A1'): 1 - 0.2,
                    ('A1', 'B1'): 1 - 0.2,
                    ('A2', 'B1'): 1 - 0.3,
                    ('A3', 'B2'): 1 - 0.5,
                    ('A4', 'B2'): 1 - 0.6,
                    ('B1', 'C1'): 1 - 0.2,
                    ('B2', 'C1'): 1 - 0.3,
                    ('B3', 'C1'): 1 - 0.4,
                    ('C1', 'D1'): 1 - 0.2}
    edges = [('Z1', 'A1'),
             ('A1', 'B1'),
             ('A2', 'B1'),
             ('A3', 'B2'),
             ('A4', 'B2'),
             ('B1', 'C1'),
             ('B2', 'C1'),
             ('B3', 'C1'),
             ('C1', 'D1')]
    signed_edges = [
        ('Z1', 'A1', INT_PLUS),   # 1
        ('Z1', 'A1', INT_MINUS),  # 2
        ('A1', 'B1', INT_PLUS),   # 3
        ('A2', 'B1', INT_MINUS),  # 4
        ('B1', 'C1', INT_PLUS),   # 5
        ('A3', 'B2', INT_PLUS),   # 6
        ('A4', 'B2', INT_MINUS),  # 7
        ('B2', 'C1', INT_PLUS),   # 8
        ('B2', 'C1', INT_MINUS),  # 9
        ('B3', 'C1', INT_MINUS),  # 10
        ('C1', 'D1', INT_PLUS),   # 11
        ('C1', 'D1', INT_MINUS),  # 12
    ]
    all_ns = set()
    for e in edges:
        all_ns.add(e[0][0].lower())
        all_ns.add(e[1][0].lower())
    hashes = {
        ('A1', 'B1') : [11],
        ('B1', 'C1') : [12, 22],
        ('B3', 'C1') : [13],
        ('B2', 'C1') : [21],
        ('A2', 'B1') : [23],
        ('A3', 'B2') : [24],
        ('A4', 'B2') : [25],
    }

    return edges, signed_edges, edge_beliefs, list(all_ns), hashes


def _setup_signed_graph():
    edges, signed_edges, edge_beliefs, all_ns, hashes = _digraph_setup()
    seg = nx.MultiDiGraph()

    seg.add_edges_from(signed_edges)
    # ATTN!! seg.edges yields u, v, index while seg.edges() yields u, v
    for u, v, sign in seg.edges:
        seg.edges[(u, v, sign)]['sign'] = sign
        seg.edges[(u, v, sign)]['belief'] = edge_beliefs[(u, v)]

    for node, data in seg.nodes(data=True):
        data['ns'] = node[0]
        data['id'] = node[1]

    sng = signed_edges_to_signed_nodes(graph=seg, prune_nodes=True,
                                       copy_edge_data=True)
    for u, v in sng.edges:
        sng.edges[(u, v)]['weight'] = -np.log(sng.edges[(u, v)]['belief'])
    
    seg.graph['hashes'] = hashes
    sng.graph['hashes'] = hashes


def test_signed_bfs():
    seg, sng, all_ns = _setup_signed_graph()
    # D1 being upregulated: 13 paths
    paths = [p for p in bfs_search(
        g=sng, source_node=('D1', INT_PLUS), reverse=True, depth_limit=5,
        node_filter=all_ns, sign=INT_PLUS)
    ]

```
