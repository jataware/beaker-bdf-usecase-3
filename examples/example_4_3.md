# Description
Render the statement hierarchy as a pygraphviz graph.

# Code
```
import logging
import networkx as nx
from indra.util import fast_deepcopy
from indra.statements import *
from indra.ontology.bio import bio_ontology
import pygraphviz as pgv
from indra.assemblers.english import EnglishAssembler

from indra.ontology.bio import bio_ontology
braf = Agent('BRAF')
map2k1 = Agent('MAP2K1')
st1 = Phosphorylation(braf, map2k1)
st2 = Phosphorylation(braf, map2k1, residue='S')
pa = Preassembler(bio_ontology, [st1, st2])
pa.combine_related() # doctest:+ELLIPSIS
MAP2K1(), S)]
graph = render_stmt_graph(pa.related_stmts)
graph.write('example_graph.dot') # To make the DOT file

```
