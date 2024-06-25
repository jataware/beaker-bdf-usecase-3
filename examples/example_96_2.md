# Description
Test the exclusion of specific statement types during graph assembly.

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

def test_exclude_stmts():
    ia = IndraNetAssembler([st1, st2, st3])
    # First assemble with dataframe method
    g = ia.make_model(method='df', exclude_stmts=['Inhibition'])
    assert len(g.nodes) == 3
    assert len(g.edges) == 2
    assert 'c' not in g.nodes
    assert ('a', 'c', 0) not in g.edges
    # Get same result assembling with preassembly
    g = ia.make_model(method='preassembly', exclude_stmts=['Inhibition'])
    assert len(g.nodes) == 3
    assert len(g.edges) == 2
    assert 'c' not in g.nodes

```
