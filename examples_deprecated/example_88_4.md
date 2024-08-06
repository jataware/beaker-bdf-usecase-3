# Description
A test to standardize the mapping of CHEBI and HMDB references.

# Code
```
from indra.preassembler.grounding_mapper import default_mapper as gm

def test_map_standardize_chebi_hmdb():
    a1 = Agent('X', db_refs={'HMDB': 'HMDB0000122'})
    a2 = Agent('Y', db_refs={'CHEBI': 'CHEBI:15903'})
    stmt = Phosphorylation(a1, a2)
    mapped_stmts = gm.map_stmts([stmt])
    assert len(mapped_stmts) == 1
    st = mapped_stmts[0]
    assert st.enz.db_refs['CHEBI'] == st.sub.db_refs['CHEBI'], \
        (st.enz.db_refs, st.sub.db_refs)
    assert st.enz.name == 'beta-D-glucose', st.enz

```
