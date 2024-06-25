# Description
De-duplicate and combine evidence for two statements differing only in their evidence lists.

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
map2k1 = Agent('MAP2K1')
mapk1 = Agent('MAPK1')
stmt1 = Phosphorylation(map2k1, mapk1, 'T', '185',
evidence=[Evidence(text='evidence 1')])
stmt2 = Phosphorylation(map2k1, mapk1, 'T', '185',
evidence=[Evidence(text='evidence 2')])
pa = Preassembler(bio_ontology)
uniq_stmts = pa.combine_duplicate_stmts([stmt1, stmt2])
uniq_stmts
MAPK1(), T, 185)]
sorted([e.text for e in uniq_stmts[0].evidence])

```
