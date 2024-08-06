# Description
A test for Gilda disambiguation in local mode.

# Code
```
indra.statements import Agent, Phosphorylation, Evidence
indra.preassembler.grounding_mapper import default_mapper as gm

@pytest.mark.nonpublic
def test_gilda_disambiguation_local():
    gm.gilda_mode = 'local'
    er1 = Agent('NDR1', db_refs={'TEXT': 'NDR1'})
    pmid1 = '18362890'
    stmt1 = Phosphorylation(None, er1,
                            evidence=[Evidence(pmid=pmid1,
                                               text_refs={'PMID': pmid1})])
    mapped_stmts1 = gm.map_stmts([stmt1])
    annotations = mapped_stmts1[0].evidence[0].annotations
    assert annotations['agents']['gilda'][0] is None
    assert annotations['agents']['gilda'][1] is not None
    assert len(annotations['agents']['gilda'][1]) == 2, \
        annotations
    # This is to make sure the to_json of the ScoredMatches works

```
