# Description
Test the assembly of a graph allowing large complexes to be included.

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
st1 = Activation(Agent('a', db_refs={'HGNC': '1'}), Agent('b'), evidence=[ev1])

def test_complex_members():
    ia = IndraNetAssembler([st1, st6])
    # First assemble with dataframe method
    g = ia.make_model(method='df', complex_members=4)
    assert len(g.nodes) == 5
    assert len(g.edges) == 13, len(g.edges)
    assert ('h', 'i', 0) in g.edges
    assert ('i', 'h', 0) in g.edges
    # Get same result assembling with preassembly
    g = ia.make_model(method='preassembly', complex_members=4)
    assert len(g.nodes) == 5
    assert len(g.edges) == 13, len(g.edges)
    assert ('h', 'i', 0) in g.edges

```
