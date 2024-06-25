# Description
Test conversion of Kappa contact map JSON to a graph and validate the graph.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
json
os import path

def test_kappy_contact_json_to_graph():
    with open(path.join(path.dirname(path.abspath(__file__)),
                        'kappy_contact.json'), 'r') as f:
        cmap = json.load(f)
    graph = cm_json_to_graph(cmap)
    assert graph is not None, 'No graph produced.'
    n_nodes = len(graph.nodes())
    n_edges = len(graph.edges())
    n_subgraphs = len(graph.subgraphs())
    assert n_nodes == 6, \
        'Wrong number (%d vs. %d) of nodes on the graph.' % (n_nodes, 6)
    assert n_edges == 3, \
        "Wrong number (%d vs. %d) of edges on graph." % (n_edges, 3)
    assert n_subgraphs == 4, \

```
