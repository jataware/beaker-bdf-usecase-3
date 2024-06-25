# Description
Testing the mapping of autophosphorylation sites and verifying the mapped modifications.

# Code
```
protmapper import MappedSite
indra.statements import *
indra.util import unicode_strs
indra.preassembler.sitemapper import default_mapper as sm, MappedStatement

def test_site_map_selfmodification():
    mapk1_invalid = Agent('MAPK1',
                          mods=[ModCondition('phosphorylation', 'T', '183')],
                          db_refs={'UP': 'P28482'})
    st1 = Autophosphorylation(mapk1_invalid, 'Y', '185')
    (valid, mapped) = sm.map_sites([st1])
    assert len(valid) == 0
    assert len(mapped) == 1
    mapped_stmt = mapped[0]
    mm = mapped_stmt.mapped_mods
    assert (mm[0].gene_name, mm[0].orig_res, mm[0].orig_pos, mm[0].mapped_res,
            mm[0].mapped_pos) == ('MAPK1', 'T', '183', 'T', '185')
    assert (mm[1].gene_name, mm[1].orig_res, mm[1].orig_pos, mm[1].mapped_res,
            mm[1].mapped_pos) == ('MAPK1', 'Y', '185', 'Y', '187')
    ms = mapped_stmt.mapped_stmt
    agent1 = ms.enz
    assert agent1.mods[0].matches(ModCondition('phosphorylation', 'T', '185'))
    assert ms.residue == 'Y'
    assert ms.position == '187'

```
