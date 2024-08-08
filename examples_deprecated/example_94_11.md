# Description
Add statements with partially grounded agents and perform preassembly with 'grounding' filter, expecting assembled statements.

# Code
```
indra.statements import *
indra.tools.incremental_model import IncrementalModel

def test_grounding_none_agent():
    im = IncrementalModel()
    im.add_statements('12345', stmts2)
    im.preassemble(filters=['grounding'])

```
