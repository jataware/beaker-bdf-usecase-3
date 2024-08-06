# Description
A test for Adeft grounding of non-positive labels.

# Code
```
from indra.preassembler.grounding_mapper import default_mapper as gm

def test_adeft_mapping_non_pos():
    er = Agent('ER', db_refs={'TEXT': 'ER'})
    # This is an exact definition of a pos_label entry so we
    # expect that it will be applied as a grounding even though the
    # Adeft model has low precision for this label.
    ev = Evidence(text='estradiol (ER)')
    stmt = Phosphorylation(None, er, evidence=[ev])
    mapped_stmt = gm.map_stmts([stmt])[0]
    assert 'CHEBI' in mapped_stmt.sub.db_refs, mapped_stmt.evidence
    # This one is not an exact definition so we expect the grounding to
    # be stripped out.
    ev = Evidence(text='Estradiol is one of the three estrogen hormones'
                  'naturally produced in the body.')
    stmt = Phosphorylation(None, er, evidence=[ev])
    mapped_stmt = gm.map_stmts([stmt])[0]
    assert 'CHEBI' not in mapped_stmt.sub.db_refs, mapped_stmt.evidence
    # This is a non-positive label, and we expect it to be stripped out
    # whether it's an exact definition or not.
    pcs = Agent('PCS', db_refs={'TEXT': 'PCS', 'MESH': 'xxx'})
    ev = Evidence(text='physical component summary (PCS)')
    stmt = Phosphorylation(None, pcs, evidence=[ev])
    mapped_stmt = gm.map_stmts([stmt])[0]
    assert 'MESH' not in mapped_stmt.sub.db_refs, \
        (mapped_stmt.sub.db_refs, mapped_stmt.evidence)
    ev = Evidence(text='physical component summary')
    stmt = Phosphorylation(None, pcs, evidence=[ev])
    mapped_stmt = gm.map_stmts([stmt])[0]
    assert 'MESH' not in mapped_stmt.sub.db_refs, \

```
