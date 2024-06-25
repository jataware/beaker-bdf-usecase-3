# Description
Add a statement with partially grounded agents and perform preassembly with 'grounding' filter.

# Code
```
from indra.statements import *

def test_grounding_not_all():
    im = IncrementalModel()
    stmt = Complex([Agent('A', db_refs={'UP': 'ABCD'}), 
                   Agent('B')])
    im.add_statements('12345', [stmt])
    im.preassemble(filters=['grounding'])

```
