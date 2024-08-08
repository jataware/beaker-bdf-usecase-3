# Description
A simple test mapping an agent's references using the default grounding mapper.

# Code
```
from indra.preassembler.grounding_mapper import default_mapper as gm

def test_simple_mapping():
    akt = Agent('pkbA', db_refs={'TEXT': 'Akt', 'UP': 'XXXXXX'})
    stmt = Phosphorylation(None, akt)
    mapped_stmts = gm.map_stmts([stmt])
    assert len(mapped_stmts) == 1
    mapped_akt = mapped_stmts[0].sub
    assert mapped_akt.db_refs['TEXT'] == 'Akt'

```
