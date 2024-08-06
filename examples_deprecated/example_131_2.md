# Description
Testing the mapping of phosphorylation modifications on multiple agents and verifying the modified statements.

# Code
```
protmapper import MappedSite
indra.statements import *
indra.util import unicode_strs
indra.preassembler.sitemapper import default_mapper as sm, MappedStatement

def test_site_map_modification():
    mapk1_invalid = Agent('MAPK1',
                          mods=[ModCondition('phosphorylation', 'T', '183'),
                                ModCondition('phosphorylation', 'Y', '185')],
                          db_refs={'UP': 'P28482'})
    mapk3_invalid = Agent('MAPK3',
                          mods=[ModCondition('phosphorylation', 'T', '201')],
                          db_refs={'UP': 'P27361'})
    map2k1_invalid = Agent('MAP2K1',
                           mods=[ModCondition('phosphorylation', 'S', '217'),
                                 ModCondition('phosphorylation', 'S', '221')],
                           db_refs={'UP': 'Q02750'})

    st1 = Phosphorylation(mapk1_invalid, mapk3_invalid, 'Y', '203')
    st2 = Phosphorylation(map2k1_invalid, mapk1_invalid, 'Y', '218')
    res = sm.map_sites([st1, st2])

    assert len(res) == 2
    valid_stmts, mapped_stmts = res
    assert isinstance(valid_stmts, list)
    assert isinstance(mapped_stmts, list)
    assert len(valid_stmts) == 0
    assert len(mapped_stmts) == 2
    # MAPK1 -> MAPK3
    mapped_stmt1 = mapped_stmts[0]
    assert isinstance(mapped_stmt1, MappedStatement)
    assert mapped_stmt1.original_stmt == st1
    assert isinstance(mapped_stmt1.mapped_mods, list)
    assert len(mapped_stmt1.mapped_mods) == 4, mapped_stmt1.mapped_mods
    ms = mapped_stmt1.mapped_stmt
    assert isinstance(ms, Statement)
    agent1 = ms.enz
    agent2 = ms.sub
    assert agent1.name == 'MAPK1'
    assert len(agent1.mods) == 2
    assert agent1.mods[0].matches(ModCondition('phosphorylation', 'T', '185'))
    assert agent1.mods[1].matches(ModCondition('phosphorylation', 'Y', '187'))
    assert agent2.mods[0].matches(ModCondition('phosphorylation', 'T', '202'))
    assert ms.residue == 'Y'
    assert ms.position == '204'

    # MAP2K1 -> MAPK1
    mapped_stmt2 = mapped_stmts[1]
    assert isinstance(mapped_stmt2, MappedStatement)
    assert mapped_stmt2.original_stmt == st2
    assert isinstance(mapped_stmt2.mapped_mods, list)
    assert len(mapped_stmt2.mapped_mods) == 5, mapped_stmt2.mapped_mods
    ms = mapped_stmt2.mapped_stmt
    assert isinstance(ms, Statement)
    agent1 = ms.enz
    agent2 = ms.sub
    assert agent1.name == 'MAP2K1'
    assert len(agent1.mods) == 2
    assert agent1.mods[0].matches(ModCondition('phosphorylation', 'S', '218'))
    assert agent1.mods[1].matches(ModCondition('phosphorylation', 'S', '222'))
    assert len(agent2.mods) == 2
    assert agent2.mods[0].matches(ModCondition('phosphorylation', 'T', '185'))
    assert agent2.mods[1].matches(ModCondition('phosphorylation', 'Y', '187'))
    # The incorrect phosphorylation residue is passed through to the new
    # statement unchanged
    assert ms.residue == 'Y'
    assert ms.position == '218'
    # Check for unicode
    assert unicode_strs((mapk1_invalid, mapk3_invalid, map2k1_invalid, st1,

```
