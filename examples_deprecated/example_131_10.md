# Description
Testing site mapping within a BoundCondition

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
    return (mapk1_invalid, mapk3_invalid)

def validate_mapk1(agent1):
    assert agent1.name == 'MAPK1'
    assert len(agent1.mods) == 2
    assert agent1.mods[0].matches(ModCondition('phosphorylation', 'T', '185'))

def test_site_map_within_bound_condition():
    # Here, we test to make sure that agents within a bound condition are
    # site-mapped
    (mapk1_invalid, mapk3_invalid) = get_invalid_mapks()

    # Add an agent to the bound condition for the object of the statement
    mapk3_invalid.bound_conditions = [BoundCondition(mapk1_invalid)]
    st1 = Activation(mapk1_invalid, mapk3_invalid, 'kinase')

    # Map sites
    res = sm.map_sites([st1])

    # Extract the mapped statement
    mapped_statements = res[1]
    assert len(mapped_statements) == 1
    mapped_s = mapped_statements[0].mapped_stmt

    # Verify that the agent in the object's bound condition got site-mapped

```
