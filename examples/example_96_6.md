# Description
Test the conversion of IndraNet to a directed graph, ensuring the correct beliefs and weights.

# Code
```
import numpy as np
import pandas as pd
import networkx as nx
from indra.statements import *
from indra.assemblers.indranet.net import default_sign_dict
from indra.assemblers.indranet import IndraNetAssembler, IndraNet

ab1 = Activation(Agent('a'), Agent('b'), evidence=[Evidence(source_api='sparser')])
ab2 = Phosphorylation(Agent('a'), Agent('b'), evidence=[Evidence(source_api='sparser'), Evidence(source_api='reach')])
ab3 = Inhibition(Agent('a'), Agent('b'), evidence=[Evidence(source_api='sparser'), Evidence(source_api='reach')])
ab4 = IncreaseAmount(Agent('a'), Agent('b'), evidence=[Evidence(source_api='trips')])
bc1 = Activation(Agent('b'), Agent('c'), evidence=[Evidence(source_api='trips')])
bc2 = Inhibition(Agent('b'), Agent('c'), evidence=[Evidence(source_api='trips'), Evidence(source_api='reach')])
bc3 = IncreaseAmount(Agent('b'), Agent('c'), evidence=[Evidence(source_api='sparser'), Evidence(source_api='reach')])

def test_to_digraph():
    ia = IndraNetAssembler([ab1, ab2, ab3, ab4, bc1, bc2, bc3, bc4])
    df = ia.make_df()
    net = IndraNet.from_df(df)
    assert len(net.nodes) == 3
    assert len(net.edges) == 8
    digraph = net.to_digraph(weight_mapping=_weight_mapping)
    assert len(digraph.nodes) == 3
    assert len(digraph.edges) == 2
    assert set([
        stmt['stmt_type'] for stmt in digraph['a']['b']['statements']]) == {
            'Activation', 'Phosphorylation', 'Inhibition', 'IncreaseAmount'}
    assert all(digraph.edges[e].get('belief', False) for e in digraph.edges)
    assert all(isinstance(digraph.edges[e]['belief'],
                          (float, np.longdouble)) for e in digraph.edges)
    assert all(digraph.edges[e].get('weight', False) for e in digraph.edges)
    assert all(isinstance(digraph.edges[e]['weight'],
                          (float, np.longdouble)) for e in digraph.edges)
    digraph_from_df = IndraNet.digraph_from_df(df)

```
