# Description
Add statements to an IncrementalModel and perform preassembly with 'prior_one' filter.

# Code
```
indra.statements import *
indra.tools.incremental_model import IncrementalModel

def test_add_stmts_blank_noprior():
    im = IncrementalModel()
    im.add_statements('12345', stmts)
    im.preassemble(filters=['prior_one'])

```
