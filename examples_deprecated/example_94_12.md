# Description
Add human-only statements to IncrementalModel and perform preassembly with 'human_only' filter.

# Code
```
from indra.statements import *

def test_human_only():
    im = IncrementalModel()
    stmt1 = Phosphorylation(None, Agent('BRAF', db_refs={'UP': 'P15056'}))
    stmt2 = Phosphorylation(None, Agent('BRAF', db_refs={'UP': 'P28028'}))
    stmt3 = Phosphorylation(None, Agent('BRAF', db_refs={'HGNC': '1097'}))
    stmt4 = Phosphorylation(None, Agent('BRAF', db_refs={}))
    im.add_statements('12345', [stmt1])
    im.preassemble(filters=['human_only'])
    assert len(im.assembled_stmts) == 1
    im.add_statements('12346', [stmt2])
    im.preassemble(filters=['human_only'])
    assert len(im.assembled_stmts) == 1
    im.add_statements('12346', [stmt3])
    im.preassemble(filters=['human_only'])
    assert len(im.assembled_stmts) == 1
    im.add_statements('12346', [stmt4])
    im.preassemble(filters=['human_only'])
    assert len(im.assembled_stmts) == 2, \

```
