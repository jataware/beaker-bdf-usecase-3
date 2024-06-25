# Description
Add statements to an IncrementalModel and perform preassembly without any filters.

# Code
```
indra.statements import *
indra.tools.incremental_model import IncrementalModel

def test_add_stmts_blank_nofilter():
    im = IncrementalModel()
    im.add_statements('12345', stmts)
    im.preassemble(filters=None)

```
