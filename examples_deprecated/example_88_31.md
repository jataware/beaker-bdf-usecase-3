# Description
A test for handling None values in agent TEXT references.

# Code
```
from indra.statements import Agent, Phosphorylation

def test_none_text_corner_case():
    ag = Agent('x', db_refs={'TEXT': None, 'TEXT_NORM': None})
    stmt = Phosphorylation(None, ag)
    res = gm.map_stmts([stmt])

```
