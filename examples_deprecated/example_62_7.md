# Description
Test the extraction of activity regulation statements from a BioPAX file using INDRA.

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

def test_activity_regulation_extraction():
    br = 'Catalysis_5710598d0317be9d4742b469d1322a48'
    stmts = list(stmts_by_source_id[br])
    assert len(stmts) == 3, stmts
    assert {s.subj.name for s in stmts} == {'HRAS', 'NRAS', 'KRAS'}
    assert isinstance(stmts[0], Activation)

```
