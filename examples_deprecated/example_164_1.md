# Description
This example demonstrates how to create a PyBEL graph from a set of INDRA Statements and to access node/edge information from the graph.

# Code
```
from indra.statements import *

    >>> from indra.statements import *
    >>> map2k1 = Agent('MAP2K1', db_refs={'HGNC': '6840'})
    >>> mapk1 = Agent('MAPK1', db_refs={'HGNC': '6871'})
    >>> stmt = Phosphorylation(map2k1, mapk1, 'T', '185')
    >>> pba = PybelAssembler([stmt])
    >>> belgraph = pba.make_model()
    >>> sorted(node.as_bel() for node in belgraph)
    ['p(HGNC:6840 ! MAP2K1)', 'p(HGNC:6871 ! MAPK1)', 'p(HGNC:6871 ! MAPK1, pmod(go:0006468 ! "protein phosphorylation", Thr, 185))']
    >>> len(belgraph)
    3
    >>> belgraph.number_of_edges()

```
