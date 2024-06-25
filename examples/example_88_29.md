# Description
A test for grounding priority when using Gilda in web mode.

# Code
```
from indra.preassembler.grounding_mapper import default_mapper as gm

def test_grounding_map_gilda_priority():
    gm.gilda_mode = 'web'
    fetal_bovine_serum = Agent('FBS', db_refs={'TEXT': 'FBS'})
    pmid = '28536624'
    stmt = Phosphorylation(None, fetal_bovine_serum,
                           evidence=[Evidence(pmid=pmid,
                                              text_refs={'PMID': pmid})])
    mapped_stmts = gm.map_stmts([stmt])
    annotations = mapped_stmts[0].evidence[0].annotations
    # agents should not be in annotations if gilda is run. Second condition
    # added as future proofing in case some future change causes this mapping
    # to add agent annotations in the future.
    assert 'agents' not in annotations or \

```
