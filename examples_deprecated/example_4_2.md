# Description
A more general statement with no information about a Phosphorylation site is identified as supporting a more specific statement.

# Code
```
import time
import tqdm
import logging
import itertools
import functools
import collections
import networkx as nx
from indra.util import fast_deepcopy
from indra.statements import *
from indra.statements import stmt_type as indra_stmt_type
from indra.ontology.bio import bio_ontology

from indra.ontology.bio import bio_ontology
braf = Agent('BRAF')
map2k1 = Agent('MAP2K1')
st1 = Phosphorylation(braf, map2k1)
st2 = Phosphorylation(braf, map2k1, residue='S')
pa = Preassembler(bio_ontology, [st1, st2])
combined_stmts = pa.combine_related() # doctest:+ELLIPSIS
combined_stmts
MAP2K1(), S)]
combined_stmts[0].supported_by
MAP2K1())]
combined_stmts[0].supported_by[0].supports

```
