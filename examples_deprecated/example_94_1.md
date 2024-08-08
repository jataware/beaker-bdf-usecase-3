# Description
Add statements to an empty IncrementalModel and perform preassembly with default filters.

# Code
```
indra.statements import *
indra.tools.incremental_model import IncrementalModel

def test_add_stmts_blank():
    im = IncrementalModel()
    im.add_statements('12345', stmts)
    assert len(im.get_statements()) == 2
    im.preassemble()

```
