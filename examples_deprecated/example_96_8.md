# Description
Test the initial signs of events within the IndraNet graph.

# Code
```
import numpy as np
import pandas as pd
import networkx as nx
from indra.statements import *
from indra.assemblers.indranet.net import default_sign_dict
from indra.assemblers.indranet import IndraNetAssembler, IndraNet


a = Event(Concept('a'), QualitativeDelta(polarity=1))
b = Event(Concept('b'), QualitativeDelta(polarity=1))
c = Event(Concept('c'), QualitativeDelta(polarity=-1))
d = Event(Concept('d'), QualitativeDelta(polarity=-1))
st1 = Influence(a, b)
st2 = Influence(b, c)
st3 = Influence(c, d)

def test_initial_signs():
    a = Event(Concept('a'), QualitativeDelta(polarity=1))
    b = Event(Concept('b'), QualitativeDelta(polarity=1))
    c = Event(Concept('c'), QualitativeDelta(polarity=-1))
    d = Event(Concept('d'), QualitativeDelta(polarity=-1))
    st1 = Influence(a, b)
    st2 = Influence(b, c)
    st3 = Influence(c, d)
    st4 = Influence(b, d)
    ia = IndraNetAssembler([st1, st2, st3, st4])
    sg = ia.make_model(graph_type='signed')
    assert len(sg.nodes) == 4
    assert len(sg.edges) == 4
    assert ('a', 'b', 0) in sg.edges
    assert ('b', 'c', 0) not in sg.edges
    assert ('b', 'c', 1) in sg.edges
    assert ('c', 'd', 0) in sg.edges
    assert ('c', 'd', 1) not in sg.edges
    assert ('b', 'd', 0) not in sg.edges

```
