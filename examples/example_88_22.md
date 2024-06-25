# Description
A test for grounding statements correctly even with misgrounding.

# Code
```
from indra.preassembler.grounding_mapper import default_mapper as gm

def test_misgrounding():
    baz1 = Agent('ZNF214', db_refs={'TEXT': 'baz1', 'HGNC': '13006'})
    stmt = Phosphorylation(None, baz1)
    stmts = gm.map_stmts([stmt])
    stmt = stmts[0]
    assert len(stmt.sub.db_refs) == 1, stmt.sub.db_refs
    assert stmt.sub.db_refs['TEXT'] == 'baz1'

```
