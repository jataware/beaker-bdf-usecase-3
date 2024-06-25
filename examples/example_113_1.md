# Description
Test breadth-first search (BFS) algorithm on an unsigned graph.

# Code
```
import numpy as np
import networkx as nx

from indra.explanation.pathfinding.pathfinding import bfs_search
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

def test_bfs():
    dg, all_ns = _setup_unsigned_graph()

    # Test basic part of algorithm
    paths = [p for p in bfs_search(dg, 'C1', depth_limit=1, reverse=True)]
    assert len(paths) == 3, len(paths)
    paths = [p for p in bfs_search(dg, 'C1', depth_limit=2, reverse=True)]
    assert len(paths) == 7, len(paths)
    paths = [p for p in bfs_search(dg, 'C1', depth_limit=2, reverse=True,
                                   path_limit=4)]
    assert len(paths) == 4, len(paths)

    # Test ns allowance list
    ans = ['c', 'b']
    assert len([p for p in
                bfs_search(dg, 'C1', depth_limit=2, reverse=True,
                           node_filter=ans)]) == 3
    assert all(len(p) < 3 for p in
               bfs_search(dg, 'C1', depth_limit=2, reverse=True,
                          node_filter=ans))

    # Test longer paths
    assert len([p for p in bfs_search(dg, 'D1', depth_limit=5,
                                      reverse=True)]) == 9

    # Test node blacklist
    assert len([p for p in bfs_search(dg, 'D1', depth_limit=5, reverse=True,
                                      node_blacklist={'Z1'})]) == 8

    # Test max per node option
    # Should get 4 paths with max_per_node=1
    expected_paths = {('D1', 'C1'), ('D1', 'C1', 'B1'),
                      ('D1', 'C1', 'B1', 'A1'),
                      ('D1', 'C1', 'B1', 'A1', 'Z1')}
    paths = [p for p in bfs_search(dg, 'D1', depth_limit=5,
                                   reverse=True, max_per_node=1,
                                   node_filter=all_ns)]
    assert len(paths) == 4, len(paths)
    assert set(paths) == expected_paths, 'sets of paths not equal'

    # Test terminal NS
    # Terminate on 'b'
    expected_paths = {('D1', 'C1', 'B1'), ('D1', 'C1', 'B2'),
                      ('D1', 'C1', 'B3')}
    paths = [p for p in bfs_search(dg, 'D1', depth_limit=5,
                                   reverse=True, terminal_ns=['b'],
                                   node_filter=all_ns)]
    assert len(paths) == len(expected_paths), len(paths)
    assert set(paths) == expected_paths, 'sets of paths not equal'

    # Terminate on 'a'
    expected_paths = {('D1', 'C1', 'B1', 'A1'), ('D1', 'C1', 'B1', 'A2'),
                      ('D1', 'C1', 'B2', 'A3'), ('D1', 'C1', 'B2', 'A4')}
    paths = [p for p in bfs_search(dg, 'D1', depth_limit=5,
                                   reverse=True, terminal_ns=['a'],
                                   node_filter=all_ns)]
    assert len(paths) == len(expected_paths), len(paths)
    assert set(paths) == expected_paths, 'sets of paths not equal'

    # Test memory limit; a very low number should yield one path
    error = False
    gen = bfs_search(dg, 'D1', depth_limit=5, reverse=True, max_memory=16)
    _ = next(gen)
    try:
        _ = next(gen)
    except (RuntimeError, StopIteration):
        error = True
    assert error

    # Test edge filter
    # With belief cutoff at 0.75, we should remove:
    # ('A2', 'B1'), ('A3', 'B2'), ('A4', 'B2'), ('B2', 'C1'), ('B3', 'C1')
    def _filter_func(g, u, v):
        return g.edges[u, v]['belief'] > 0.75

    expected_paths = {('D1', 'C1'), ('D1', 'C1', 'B1'),
                      ('D1', 'C1', 'B1', 'A1'),
                      ('D1', 'C1', 'B1', 'A1', 'Z1')}
    gen = bfs_search(g=dg, source_node='D1', depth_limit=5, reverse=True,
                     edge_filter=_filter_func)
    paths = list(gen)
    assert len(paths) == len(expected_paths), f'Expected ' \
                                              f'{len(expected_paths)}, ' \
                                              f'got {len(paths)} paths'
    assert set(paths) == expected_paths

    # Test edge_filter and allowed_edges
    def _alwd_edges(u, v):
        # Edges should not be reversed!
        return (u, v) in {('C1', 'D1'), ('B1', 'C1'), ('A1', 'B1')}
    expected_paths = {('D1', 'C1'), ('D1', 'C1', 'B1'),
                      ('D1', 'C1', 'B1', 'A1')}
    some_new_gen = bfs_search(g=dg, source_node='D1', depth_limit=5,
                              reverse=True, edge_filter=_filter_func,
                              allow_edge=_alwd_edges, hashes=[123456897],
                              strict_mesh_id_filtering=True)
    paths = list(some_new_gen)
    assert len(paths) == len(expected_paths), f'Expected ' \
                                              f'{len(expected_paths)}, ' \
                                              f'got {len(paths)} paths'

```
