# Description
A test ensuring that the mapper grounds agents within a bound condition.

# Code
```
from indra.preassembler.grounding_mapper import default_mapper as gm

def test_bound_condition_mapping():
    # Verify that the grounding mapper grounds the agents within a bound
    # condition
    akt = Agent('pkbA', db_refs={'TEXT': 'Akt', 'UP': 'XXXXXX'})
    erk = Agent('ERK1', db_refs={'TEXT': 'ERK1'})
    akt.bound_conditions = [BoundCondition(erk)]

    stmt = Phosphorylation(None, akt)

    mapped_stmts = gm.map_stmts([stmt])

    s = mapped_stmts[0]
    mapped_akt = mapped_stmts[0].sub
    mapped_erk = mapped_akt.bound_conditions[0].agent

    assert mapped_akt.db_refs['TEXT'] == 'Akt'
    assert mapped_akt.db_refs['FPLX'] == 'AKT'

    assert mapped_erk.db_refs['TEXT'] == 'ERK1'
    assert mapped_erk.db_refs['HGNC'] == '6877'

```
