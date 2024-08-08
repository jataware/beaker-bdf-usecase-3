# Description
A test of multiple bound conditions.

# Code
```
from indra.preassembler.grounding_mapper import default_mapper as gm

def test_bound_condition_mapping_multi():
    # Test with multiple agents
    akt = Agent('pkbA', db_refs={'TEXT': 'Akt', 'UP': 'XXXXXX'})
    erk = Agent('ERK1', db_refs={'TEXT': 'ERK1'})
    akt.bound_conditions = [BoundCondition(erk)]
    stmt = Phosphorylation(akt, erk)
    mapped_stmts = gm.map_stmts([stmt])
    s = mapped_stmts[0]
    mapped_akt = mapped_stmts[0].enz
    mapped_erk1 = mapped_akt.bound_conditions[0].agent
    mapped_erk2 = mapped_stmts[0].sub

    assert mapped_akt.db_refs['TEXT'] == 'Akt'
    assert mapped_akt.db_refs['FPLX'] == 'AKT'

    for e in (mapped_erk1, mapped_erk2):
        assert e.db_refs['TEXT'] == 'ERK1'
        assert e.db_refs['HGNC'] == '6877'

```
