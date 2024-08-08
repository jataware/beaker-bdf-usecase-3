# Description
A test for grounding only ungrounded statements.

# Code
```
from indra.preassembler.grounding_mapper.gilda import ground_statement, ground_statements

def test_gilda_ground_ungrounded():
    ag1 = Agent('x', db_refs={'TEXT': 'RAS', 'FPLX': 'RAS'})
    ag2 = Agent('x', db_refs={'TEXT': 'RAS'})
    ag3 = Agent('x', db_refs={'TEXT': 'RAS', 'XXXXX': 'XXXX'})
    stmts = [Phosphorylation(None, ag) for ag in (ag1, ag2, ag3)]
    ground_statement(stmts[0], ungrounded_only=True)
    assert ag1.name == 'x'
    ground_statement(stmts[0], ungrounded_only=False)
    assert ag1.name == 'RAS', ag1
    ground_statement(stmts[1], ungrounded_only=True)
    assert ag2.name == 'RAS'
    grounded_stmts = ground_statements([stmts[2]], ungrounded_only=True)

```
