# Description
Perform graph reductions using a custom NetworkX graph function.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
import networkx

def test_graph_reductions():
    G = networkx.DiGraph([('activity', 'kinase'),
                          ('catalytic', 'kinase'),
                          ('activity', 'catalytic'),
                          ('activity', 'phosphatase'),
                          ('catalytic', 'phosphatase')])
    reductions = _get_graph_reductions(G)
    assert reductions == {'activity': 'catalytic',
                          'kinase': 'kinase',
                          'phosphatase': 'phosphatase',
                          'catalytic': 'catalytic'}
    G = networkx.DiGraph([('activity', 'kinase'),
                          ('catalytic', 'kinase'),
                          ('activity', 'catalytic')])
    reductions = _get_graph_reductions(G)
    assert reductions == {'activity': 'kinase',
                          'catalytic': 'kinase',
                          'kinase': 'kinase'}
    G = networkx.DiGraph([('activity', 'kinase'),
                          ('catalytic', 'kinase'),
                          ('activity', 'catalytic'),
                          ('activity', 'transcription')])
    reductions = _get_graph_reductions(G)
    assert reductions == {'activity': 'activity',
                          'transcription': 'transcription',
                          'catalytic': 'kinase',

```
