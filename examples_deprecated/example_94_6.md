# Description
Add one statement to IncrementalModel with prior statements and perform preassembly with 'prior_one' filter.

# Code
```
indra.statements import *
indra.tools.incremental_model import IncrementalModel

def test_add_stmts_prior_one():
    im = IncrementalModel()
    im.stmts['prior'] = [stmts[0]]
    im.prior_genes = ['MAPK1', 'MAPK3']
    im.add_statements('12345', [stmts[1]])
    im.preassemble(filters=['prior_one'])

```
