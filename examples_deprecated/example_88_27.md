# Description
A test for Gilda disambiguation in web mode.

# Code
```
indra.statements import Agent, Phosphorylation, Inhibition, Evidence
indra.preassembler.grounding_mapper import default_mapper as gm

@pytest.mark.nonpublic
def test_gilda_disambiguation():
    gm.gilda_mode = 'web'
    er1 = Agent('NDR1', db_refs={'TEXT': 'NDR1'})
    pmid1 = '18362890'
    stmt1 = Phosphorylation(None, er1,
                            evidence=[Evidence(pmid=pmid1,
                                               text_refs={'PMID': pmid1})])

    er2 = Agent('NDR1', db_refs={'TEXT': 'NDR1'})
    pmid2 = '16832411'
    stmt2 = Inhibition(None, er2,
                       evidence=[Evidence(pmid=pmid2,
                                          text_refs={'PMID': pmid2})])
    mapped_stmts1 = gm.map_stmts([stmt1])
    assert mapped_stmts1[0].sub.name == 'STK38', mapped_stmts1[0].sub.name
    assert mapped_stmts1[0].sub.db_refs['HGNC'] == '17847', \
        mapped_stmts1[0].sub.db_refs
    assert mapped_stmts1[0].sub.db_refs['UP'] == 'Q15208', \
        mapped_stmts1[0].sub.db_refs

    mapped_stmts2 = gm.map_stmts([stmt2])
    assert mapped_stmts2[0].obj.name == 'NDRG1', \
        mapped_stmts2[0].obj.name
    assert mapped_stmts2[0].obj.db_refs['HGNC'] == '7679', \
        mapped_stmts2[0].obj.db_refs
    assert mapped_stmts2[0].obj.db_refs['UP'] == 'Q92597', \
        mapped_stmts2[0].obj.db_refs

    annotations = mapped_stmts2[0].evidence[0].annotations
    assert len(annotations['agents']['gilda'][1]) == 2, \
        annotations
    assert annotations['agents']['gilda'][0] is None

```
