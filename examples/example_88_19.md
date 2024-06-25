# Description
A test for mapping agents in a complex statement.

# Code
```
from indra.preassembler.grounding_mapper import default_mapper as gm

def test_map_agent():
    erk = Agent('ERK1', db_refs={'TEXT': 'ERK1'})
    p_erk = Agent('P-ERK', db_refs={'TEXT': 'p-ERK'})
    stmt = Complex([erk, p_erk])
    mapped_stmts = gm.map_stmts([stmt])
    mapped_ag = mapped_stmts[0].members[1]
    assert mapped_ag.name == 'ERK'

```
