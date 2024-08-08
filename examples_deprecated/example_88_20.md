# Description
A test for grounding with Adeft models.

# Code
```
indra.preassembler.grounding_mapper import default_mapper as gm
indra.statements import Agent, Phosphorylation, Inhibition, Evidence

@pytest.mark.nonpublic
def test_adeft_mapping():
    er1 = Agent('ER', db_refs={'TEXT': 'ER'})
    pmid1 = '30775882'
    stmt1 = Phosphorylation(None, er1, evidence=[Evidence(pmid=pmid1,
                                                          text_refs={'PMID':
                                                                     pmid1})])

    er2 = Agent('ER', db_refs={'TEXT': 'ER'})
    pmid2 = '28369137'
    stmt2 = Inhibition(None, er2, evidence=[Evidence(pmid=pmid2,
                                                     text_refs={'PMID':
                                                                pmid2})])

    mapped_stmts1 = gm.map_stmts([stmt1])
    assert mapped_stmts1[0].sub.name == 'ESR', \
        mapped_stmts1[0].sub.name
    assert mapped_stmts1[0].sub.db_refs['FPLX'] == 'ESR', \
        mapped_stmts1[0].sub.db_refs

    mapped_stmts2 = gm.map_stmts([stmt2])
    assert mapped_stmts2[0].obj.name == 'endoplasmic reticulum', \
        mapped_stmts2[0].obj.name
    assert mapped_stmts2[0].obj.db_refs['GO'] == 'GO:0005783', \
        mapped_stmts2[0].obj.db_refs

    annotations = mapped_stmts2[0].evidence[0].annotations

```
