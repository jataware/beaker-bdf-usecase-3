# Description
A test to standardize the mapping of HGNC and UP references.

# Code
```
from indra.preassembler.grounding_mapper import default_mapper as gm

def test_map_standardize_up_hgnc():
    a1 = Agent('MAPK1', db_refs={'HGNC': '6871'})
    a2 = Agent('MAPK1', db_refs={'UP': 'P28482'})
    stmt = Phosphorylation(a1, a2)
    mapped_stmts = gm.map_stmts([stmt])
    assert len(mapped_stmts) == 1
    st = mapped_stmts[0]
    assert st.enz.db_refs['HGNC'] == st.sub.db_refs['HGNC'], \
        (st.enz.db_refs, st.sub.db_refs)

```
