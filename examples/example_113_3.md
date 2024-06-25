# Description
Test finding the shortest simple paths in an unsigned graph with modifications.

# Code
```
import numpy as np
import networkx as nx

from indra.explanation.pathfinding.pathfinding import shortest_simple_paths
from indra.explanation.pathfinding.util import get_subgraph

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


def _setup_unsigned_graph():
    edges, signed_edges, edge_beliefs, all_ns, hashes = _digraph_setup()
    dg = nx.DiGraph()
    dg.add_edges_from(edges)

    # Add belief
    for e in dg.edges:
        dg.edges[e]['belief'] = edge_beliefs[e]
        dg.edges[e]['weight'] = -np.log(edge_beliefs[e], dtype=np.longdouble)
    
    # Add edge_by_hash
    dg.graph['hashes'] = hashes

    # Add namespaces
    nodes1, nodes2 = list(zip(*edges))
    nodes = set(nodes1).union(nodes2)
    for node in nodes:
        ns = node[0]
        _id = node[1]
        dg.nodes[node]['ns'] = ns
        dg.nodes[node]['id'] = _id

def test_shortest_simple_paths_mod_unsigned():
    dg, all_ns = _setup_unsigned_graph()
    dg.add_edge('B1', 'A3', belief=0.7, weight=-np.log(0.7))  # Add long path
    # between
    # B1 and C1
    source, target = 'B1', 'D1'

    # Unweighted searches
    paths = [p for p in shortest_simple_paths(dg, source, target)]
    assert len(paths) == 2
    assert tuple(paths[0]) == ('B1', 'C1', 'D1')
    assert tuple(paths[1]) == ('B1', 'A3', 'B2', 'C1', 'D1')
    assert len([p for p in shortest_simple_paths(
        dg, source, target, ignore_nodes={'A3'})]) == 1
    # Test nx.NoPathFound
    try:
        len([p for p in shortest_simple_paths(
            dg, source, target, ignore_nodes={'C1'})]) == 0
    except Exception as exc:
        assert isinstance(exc, nx.NetworkXNoPath)

    # Weighted searches
    paths = [p for p in shortest_simple_paths(dg, source, target,
                                              weight='weight')]
    assert tuple(paths[0]) == ('B1', 'C1', 'D1')

```
