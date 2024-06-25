# Description
Test the extraction of phosphorylation events from a BioPAX file using INDRA.

# Code
```
from indra.sources import biopax
import os
from collections import defaultdict
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'biopax_test.owl')
bp = biopax.process_owl(model_path)
stmts_by_source_id = defaultdict(set)
for stmt in bp.statements:
    for ev in stmt.evidence:

def test_phosphorylation_extraction():
    cat = 'Catalysis_12411c77e2fd2252f2a8b52bbee6eeb9'
    stmts = list(stmts_by_source_id[cat])
    assert len(stmts) == 2
    assert all(isinstance(stmt, Phosphorylation) for stmt in stmts)
    assert all(stmt.enz.name == 'BRAF' for stmt in stmts)
    assert all(stmt.sub.name == 'MAP2K1' for stmt in stmts)

```
