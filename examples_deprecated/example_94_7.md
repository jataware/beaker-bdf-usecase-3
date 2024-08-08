# Description
Add one statement to IncrementalModel with prior statements and perform preassembly with 'prior_all' filter.

# Code
```
indra.statements import *
indra.tools.incremental_model import IncrementalModel

def test_add_stmts_prior_all():
    im = IncrementalModel()
    # Start out with MAPK1 and MAPK3
    im.stmts['prior'] = [stmts[0]]
    im.prior_genes = ['MAPK1', 'MAPK3']
    # Try to add MAP2K1 and MAPK3
    im.add_statements('12345', [stmts[1]])
    im.preassemble(filters=['prior_all'])

```
