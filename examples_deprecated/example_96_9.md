# Description
Test the conversion of different types of graphs, with and without self-loops, within IndraNet.

# Code
```
import numpy as np
import pandas as pd
import networkx as nx
from indra.statements import *
from indra.assemblers.indranet.net import default_sign_dict
from indra.assemblers.indranet import IndraNetAssembler, IndraNet


aa = Activation(Agent('a', db_refs={'HGNC': '1'}), Agent('a'))
ab = Inhibition(Agent('a', db_refs={'HGNC': '1'}), Agent('b'))
bc = Activation(Agent('b'), Agent('v'))
cc = Activation(Agent('c'), Agent('c'))

def test_self_loops():
    aa = Activation(Agent('a', db_refs={'HGNC': '1'}), Agent('a'))
    ab = Inhibition(Agent('a', db_refs={'HGNC': '1'}), Agent('b'))
    bc = Activation(Agent('b'), Agent('v'))
    cc = Activation(Agent('c'), Agent('c'))
    bbc = Complex([Agent('b'), Agent('b'), Agent('c')])

    ia = IndraNetAssembler([aa, ab, bc, cc, bbc])

    # Signed graph from df with self-loops
    sg1 = ia.make_model(method='df', graph_type='signed', keep_self_loops=True)
    assert ('a', 'a', 0) in sg1.edges
    assert ('c', 'c', 0) in sg1.edges
    # Complex edges are not included in signed graph
    assert ('b', 'b', 0) not in sg1.edges

    # Signed graph from preassembly with self-loops
    sg2 = ia.make_model(method='preassembly', graph_type='signed',
                        keep_self_loops=True)
    assert ('a', 'a', 0) in sg2.edges
    assert ('c', 'c', 0) in sg2.edges
    # Complex edges are not included in signed graph
    assert ('b', 'b', 0) not in sg2.edges

    # Signed graph from df without self-loops
    sg3 = ia.make_model(method='df', graph_type='signed',
                        keep_self_loops=False)
    assert ('a', 'a', 0) not in sg3.edges
    assert ('c', 'c', 0) not in sg3.edges
    assert ('b', 'b', 0) not in sg3.edges

    # Signed graph from preassembly without self-loops
    sg4 = ia.make_model(method='preassembly', graph_type='signed',
                        keep_self_loops=False)
    assert ('a', 'a', 0) not in sg4.edges
    assert ('c', 'c', 0) not in sg4.edges
    assert ('b', 'b', 0) not in sg4.edges

    # Unsigned graph from df with self-loops
    ug1 = ia.make_model(method='df', graph_type='digraph',
                        keep_self_loops=True)
    assert ('a', 'a') in ug1.edges
    assert ('c', 'c') in ug1.edges
    assert ('b', 'b') in ug1.edges

    # Unsigned graph from preassembly with self-loops
    ug2 = ia.make_model(method='preassembly', graph_type='digraph',
                        keep_self_loops=True)
    assert ('a', 'a') in ug2.edges
    assert ('c', 'c') in ug2.edges
    assert ('b', 'b') in ug2.edges

    # Unsigned graph from df without self-loops
    ug3 = ia.make_model(method='df', graph_type='digraph',
                        keep_self_loops=False)
    assert ('a', 'a') not in ug3.edges
    assert ('c', 'c') not in ug3.edges
    assert ('b', 'b') not in ug3.edges

    # Unsigned graph from preassembly without self-loops
    ug4 = ia.make_model(method='preassembly', graph_type='digraph',
                        keep_self_loops=False)
    assert ('a', 'a') not in ug4.edges
    assert ('c', 'c') not in ug4.edges

```
