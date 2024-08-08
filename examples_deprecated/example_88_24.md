# Description
A test for grounding by Gilda from specific sources.

# Code
```
from indra.preassembler.grounding_mapper.gilda import ground_statements

def test_ground_gilda_source():
    ev1 = Evidence(source_api='reach')
    ev2 = Evidence(source_api='sparser')
    ev3 = Evidence(source_api='trips')
    stmts = [Phosphorylation(None, Agent('x', db_refs={'TEXT': 'kras'}),
                             evidence=ev)
             for ev in (ev1, ev2, ev3)]
    grounded_stmts = ground_statements(stmts, sources=['trips'])
    assert grounded_stmts[0].sub.name == 'x', stmts[0]
    assert grounded_stmts[1].sub.name == 'x'
    assert grounded_stmts[2].sub.name == 'KRAS'
    grounded_stmts = ground_statements(stmts, sources=['reach', 'sparser'])
    assert all(stmt.sub.name == 'KRAS'

```
