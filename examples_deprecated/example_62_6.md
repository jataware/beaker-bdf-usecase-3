# Description
Test the extraction of amount regulation statements from a BioPAX file using INDRA.

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

def test_amount_regulation_extraction():
    br = 'TemplateReactionRegulation_77553a64e29e82b517d0be230363b757'
    stmts = list(stmts_by_source_id[br])
    assert len(stmts) == 1, stmts
    stmt = stmts[0]
    assert isinstance(stmt, IncreaseAmount)
    assert stmt.subj.name == 'reactive oxygen species'
    assert stmt.subj.db_refs['CHEBI'] == 'CHEBI:26523'

```
