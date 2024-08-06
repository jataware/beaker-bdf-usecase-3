# Description
This example demonstrates how to use the RLIMS-P webservice to process a document and ensure that certain conditions are met for the extracted statements.

# Code
```
os
unittest

def test_simple_usage():
    rp = rlimsp.process_from_webservice('PMC3717945')
    stmts = rp.statements
    assert len(stmts) == 33, len(stmts)
    for s in stmts:
        assert len(s.evidence) == 1, "Wrong amount of evidence."
        ev = s.evidence[0]
        assert ev.annotations, "Missing annotations."
        assert 'agents' in ev.annotations.keys()

```
