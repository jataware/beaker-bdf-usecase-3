# Description
Test creating IndraNet directly from a DataFrame.

# Code
```
import numpy as np
import pandas as pd
import networkx as nx
from indra.statements import *
from indra.assemblers.indranet.net import default_sign_dict
from indra.assemblers.indranet import IndraNetAssembler, IndraNet

ev1 = Evidence(pmid='1')
ev2 = Evidence(pmid='2')
ev3 = Evidence(pmid='3')
st1 = Activation(Agent('a', db_refs={'HGNC': '1'}), Agent('b'), evidence=[ev1])
st2 = Inhibition(Agent('a', db_refs={'HGNC': '1'}), Agent('c'), evidence=[ev1, ev2, ev3])
st2.belief = 0.76
st3 = Activation(Agent('b'), Agent('d'))
st4 = ActiveForm(Agent('e'), None, True)
st5 = Complex([Agent('c'), Agent('f'), Agent('g')])
st6 = Complex([Agent('h'), Agent('i'), Agent('j'), Agent('b')])
st7 = Phosphorylation(None, Agent('x'))

def test_from_df():
    ia = IndraNetAssembler([st1, st2, st3, st4, st5, st6, st7, st9])
    df = ia.make_df()
    net = IndraNet.from_df(df)
    assert len(net.nodes) == 8
    assert len(net.edges) == 10
    # Stmt with 1 agent should not be added
    assert 'e' not in net.nodes
    # Complex with more than 3 agents should not be added
    assert ('f', 'g', 0) in net.edges
    assert ('h', 'i', 0) not in net.edges
    # Test node attributes
    assert net.nodes['a']['ns'] == 'HGNC', net.nodes['a']['ns']
    assert net.nodes['a']['id'] == '1'
    # Test edge attributes
    e = net['a']['c'][0]
    assert e['stmt_type'] == 'Inhibition'
    assert e['belief'] == 0.76
    assert e['evidence_count'] == 3
    assert net['b']['d'][0]['evidence_count'] == 0
    assert net['MEK']['MAPK'][0]['residue'] == get_valid_residue('Thr')

```
