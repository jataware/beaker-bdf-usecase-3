# Description
Testing site mapping for a complex formation of agents with invalid site information.

# Code
```
from protmapper import MappedSite
from indra.statements import *
from indra.util import unicode_strs
from indra.preassembler.sitemapper import default_mapper as sm, MappedStatement
from indra.preassembler.sitemapper import _valid_position_str

def get_invalid_mapks():
    """A handy function for getting the invalid MAPK agents we want."""
    mapk1_invalid = Agent('MAPK1',
                          mods=[ModCondition('phosphorylation', 'T', '183'),
                                ModCondition('phosphorylation', 'Y', '185')],
                          db_refs={'UP': 'P28482'})
    mapk3_invalid = Agent('MAPK3',
                          mods=[ModCondition('phosphorylation', 'T', '201'),
                                ModCondition('phosphorylation', 'Y', '203')],
                          db_refs={'UP': 'P27361'})
    assert unicode_strs((mapk1_invalid, mapk3_invalid))

def test_site_map_complex():
    (mapk1_invalid, mapk3_invalid) = get_invalid_mapks()
    st1 = Complex([mapk1_invalid, mapk3_invalid])
    res = sm.map_sites([st1])

```
