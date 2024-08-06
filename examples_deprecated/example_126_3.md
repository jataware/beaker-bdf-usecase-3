# Description
This example demonstrates how to process a JSONL file with RLIMS-P and check specific attributes of the resulting statements.

# Code
```
os
unittest

def test_tyrosine_grounding():
    here = os.path.dirname(os.path.abspath(__file__))
    fname = os.path.join(here, 'rlimsp_site.json')
    rp = rlimsp.process_jsonl_file(fname)
    assert len(rp.statements) == 1
    stmt = rp.statements[0]
    assert stmt.residue == 'Y'

```
