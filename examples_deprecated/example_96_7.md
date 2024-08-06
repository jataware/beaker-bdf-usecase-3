# Description
Test the construction of a signed graph from IndraNet, evaluating edge properties and types.

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

def test_to_signed_graph():
    ia = IndraNetAssembler([ab1, ab2, ab3, ab4, bc1, bc2, bc3, bc4])
    df = ia.make_df()
    net = IndraNet.from_df(df)
    signed_graph = net.to_signed_graph(
        sign_dict=default_sign_dict,
        weight_mapping=_weight_mapping)
    assert len(signed_graph.nodes) == 3
    assert len(signed_graph.edges) == 4
    assert set([stmt['stmt_type'] for stmt in
                signed_graph['a']['b'][0]['statements']]) == {
                    'Activation', 'IncreaseAmount'}
    assert set([stmt['stmt_type'] for stmt in
                signed_graph['a']['b'][1]['statements']]) == {'Inhibition'}
    assert set([stmt['stmt_type'] for stmt in
                signed_graph['b']['c'][0]['statements']]) == {
                    'Activation', 'IncreaseAmount'}
    assert set([stmt['stmt_type'] for stmt in
                signed_graph['b']['c'][1]['statements']]) == {
                    'Inhibition', 'DecreaseAmount'}
    assert all(signed_graph.edges[e].get('belief', False) for e in
               signed_graph.edges)
    assert all(isinstance(signed_graph.edges[e]['belief'],
                          (float, np.longdouble)) for e in signed_graph.edges)
    assert all(signed_graph.edges[e].get('weight', False) for e in
               signed_graph.edges)
    assert all(isinstance(signed_graph.edges[e]['weight'],

```
