# Description
Test the extraction of active form regulations from a BioPAX file using INDRA.

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

def test_active_form_extraction():
    br = 'BiochemicalReaction_5271ab5d568f463bffa8bb378e8aa257'
    stmts = list(stmts_by_source_id[br])
    assert len(stmts) == 2, stmts
    stmt = stmts[0]
    assert isinstance(stmt, ActiveForm)
    assert stmt.agent.name in {'MAPK1', 'MAPK3'}

```
