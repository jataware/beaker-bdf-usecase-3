# Description
Calling combine_related on two statements results in one top-level statement; calling flatten_stmts recovers both.

# Code
```
indra.statements import *
indra.util import fast_deepcopy

from indra.ontology.bio import bio_ontology
braf = Agent('BRAF')
map2k1 = Agent('MAP2K1')
st1 = Phosphorylation(braf, map2k1)
st2 = Phosphorylation(braf, map2k1, residue='S')
pa = Preassembler(bio_ontology, [st1, st2])
pa.combine_related() # doctest:+ELLIPSIS
MAP2K1(), S)]
flattened = flatten_stmts(pa.related_stmts)
flattened.sort(key=lambda x: x.matches_key())
flattened

```
