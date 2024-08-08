# Description
A test with agent/json mapping.

# Code
```
from indra.preassembler.grounding_mapper import default_mapper as gm

def test_bound_condition_mapping_agent_json():
    # Test with agent/json mapping
    akt = Agent('pkbA', db_refs={'TEXT': 'p-Akt', 'UP': 'XXXXXX'})
    erk = Agent('ERK1', db_refs={'TEXT': 'ERK1'})
    akt.bound_conditions = [BoundCondition(erk)]
    stmt = Phosphorylation(None, akt)

    mapped_stmts = gm.map_stmts([stmt])

    s = mapped_stmts[0]
    mapped_akt = mapped_stmts[0].sub
    mapped_erk = mapped_akt.bound_conditions[0].agent

    #assert mapped_akt.db_refs['TEXT'] == 'p-AKT', mapped_akt.db_refs
    assert mapped_akt.db_refs['FPLX'] == 'AKT', mapped_akt.db_refs

    assert mapped_erk.db_refs['TEXT'] == 'ERK1'
    assert mapped_erk.db_refs['HGNC'] == '6877'

```
