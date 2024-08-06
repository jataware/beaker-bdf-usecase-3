# Description
Add statements to IncrementalModel and perform preassembly with 'grounding' filter, expecting no assembled statements due to grounding failures.

# Code
```
indra.statements import *
indra.tools.incremental_model import IncrementalModel

def test_grounding_none():
    im = IncrementalModel()
    im.add_statements('12345', stmts)
    im.preassemble(filters=['grounding'])

```
