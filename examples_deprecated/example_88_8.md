# Description
A test with an ignored agent.

# Code
```
from indra.preassembler.grounding_mapper import default_mapper as gm

def test_ignore():
    agent = Agent('FA', db_refs={'TEXT': 'FA'})
    stmt = Phosphorylation(None, agent)
    mapped_stmts = gm.map_stmts([stmt])

```
