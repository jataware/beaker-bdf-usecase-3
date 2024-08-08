# Description
Testing the mapping of phosphorylation sites on an agent and asserting the results.

# Code
```
protmapper import MappedSite
indra.statements import *
indra.util import unicode_strs
indra.preassembler.sitemapper import default_mapper as sm, MappedStatement

def test_check_agent_mod():
    mapk1_valid = Agent('MAPK1',
                        mods=[ModCondition('phosphorylation', 'T', '185'),
                              ModCondition('phosphorylation', 'Y', '187')],
                        db_refs={'UP': 'P28482'})
    mapped_sites_valid, _ = sm._map_agent_sites(mapk1_valid)
    assert not mapped_sites_valid, mapped_sites_valid

    mapk1_invalid = Agent('MAPK1',
                          mods=[ModCondition('phosphorylation', 'T', '183'),
                                ModCondition('phosphorylation', 'Y', '185')],
                          db_refs={'UP': 'P28482'})
    mapped_sites_invalid, new_agent = sm._map_agent_sites(mapk1_invalid)
    assert len(mapped_sites_invalid) == 2
    assert isinstance(mapped_sites_invalid[0], MappedSite)
    map183 = mapped_sites_invalid[0]
    assert (map183.up_id, map183.orig_res, map183.orig_pos,
            map183.mapped_res, map183.mapped_pos) == \
        ('P28482', 'T', '183', 'T', '185'), map183
    map185 = mapped_sites_invalid[1]
    assert (map185.up_id, map185.orig_res, map185.orig_pos,
            map185.mapped_res, map185.mapped_pos) == \
        ('P28482', 'Y', '185', 'Y', '187'), map183
    assert len(new_agent.mods) == 2
    assert new_agent.mods[0].matches(ModCondition('phosphorylation',
                                                  'T', '185'))
    assert new_agent.mods[1].matches(ModCondition('phosphorylation',
                                                  'Y', '187'))
    assert unicode_strs((mapk1_valid, mapk1_invalid, mapped_sites_invalid,

```
