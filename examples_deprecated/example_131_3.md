# Description
Testing site mapping for the activity modification of an agent.

# Code
```
protmapper import MappedSite
indra.statements import *
indra.util import unicode_strs
indra.preassembler.sitemapper import default_mapper as sm, MappedStatement

def test_site_map_activity_modification():
    mc = [ModCondition('phosphorylation', 'T', '183'),
          ModCondition('phosphorylation', 'Y', '185')]
    mapk1 = Agent('MAPK1', mods=mc, db_refs={'UP': 'P28482'})

    st1 = ActiveForm(mapk1, 'kinase', True)
    (valid, mapped) = sm.map_sites([st1])
    assert len(valid) == 0
    assert len(mapped) == 1
    ms = mapped[0]
    mm = ms.mapped_mods
    assert (mm[0].gene_name, mm[0].orig_res, mm[0].orig_pos, mm[0].mapped_res,
            mm[0].mapped_pos) == ('MAPK1', 'T', '183', 'T', '185')
    assert (mm[1].gene_name, mm[1].orig_res, mm[1].orig_pos, mm[1].mapped_res,
            mm[1].mapped_pos) == ('MAPK1', 'Y', '185', 'Y', '187')
    assert ms.original_stmt == st1
    assert ms.mapped_stmt.agent.mods[0].matches(ModCondition('phosphorylation',
                                                             'T', '185'))
    assert ms.mapped_stmt.agent.mods[1].matches(ModCondition('phosphorylation',
                                                             'Y', '187'))

```
