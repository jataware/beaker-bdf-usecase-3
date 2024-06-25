# Description
A test for grounding when UP ID but not HGNC symbol is available.

# Code
```
from indra.preassembler.grounding_mapper import GroundingMapper

def test_up_but_not_hgnc():
    erk = Agent('ERK1', db_refs={'TEXT': 'ERK1'})
    stmt = Phosphorylation(None, erk)
    g_map = {'ERK1': {'TEXT': 'ERK1', 'UP': 'P28482'}}
    gm = GroundingMapper(g_map)
    mapped_stmts = gm.map_stmts([stmt])
    assert len(mapped_stmts) == 1
    mapped_erk = mapped_stmts[0].sub
    assert mapped_erk.name == 'MAPK1'
    assert mapped_erk.db_refs['TEXT'] == 'ERK1'
    assert mapped_erk.db_refs['HGNC'] == '6871'

```
