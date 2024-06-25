# Description
Add a statement with fully grounded agents and perform preassembly with 'grounding' filter.

# Code
```
from indra.statements import *

def test_grounding_all():
    im = IncrementalModel()
    stmt = Complex([Agent('A', db_refs={'UP': 'ABCD'}), 
                   Agent('B', db_refs={'HGNC': '1234'})])
    im.add_statements('12345', [stmt])
    im.preassemble(filters=['grounding'])

```
