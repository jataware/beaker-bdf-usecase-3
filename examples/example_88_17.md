# Description
A test to ensure grounding mapper does not modify initial grounding map.

# Code
```
from indra.preassembler.grounding_mapper import GroundingMapper

def test_in_place_overwrite_of_gm():
    """Make sure HGNC lookups don't modify the original grounding map by adding
    keys."""
    erk = Agent('ERK1', db_refs={'TEXT': 'ERK1'})
    stmt = Phosphorylation(None, erk)
    g_map = {'ERK1': {'TEXT': 'ERK1', 'UP': 'P28482'}}
    gm = GroundingMapper(g_map)
    mapped_stmts = gm.map_stmts([stmt])
    gmap_after_mapping = gm.grounding_map

```
