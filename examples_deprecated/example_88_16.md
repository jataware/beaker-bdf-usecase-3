# Description
A test for grounding non-human proteins.

# Code
```
from indra.preassembler.grounding_mapper import GroundingMapper

def test_up_id_with_no_hgnc_id():
    """Non human protein"""
    gag = Agent('Gag', db_refs={'TEXT': 'Gag'})
    stmt = Phosphorylation(None, gag)
    g_map = {'Gag': {'TEXT': 'Gag', 'UP': 'P04585'}}
    gm = GroundingMapper(g_map)
    mapped_stmts = gm.map_stmts([stmt])
    assert len(mapped_stmts) == 1
    mapped_gag = mapped_stmts[0].sub
    assert mapped_gag.name == 'gag-pol'
    assert mapped_gag.db_refs['TEXT'] == 'Gag'
    assert mapped_gag.db_refs.get('HGNC') is None

```
