# Description
Fix invalidities in a list of statements using the `fix_invalidities` function and the `assemble_corpus` module.

# Code
```
from indra.statements import Agent, Evidence, Translocation, Phosphorylation
import indra.tools.assemble_corpus as ac

def test_fix_stmts():
    stmts = [Translocation(Agent('x'), to_location=None, from_location=None),
             Phosphorylation(Agent('a', db_refs={'TEXT': None,
                                                 'FPLX': 'ERK'}), Agent('b'),
                             evidence=[Evidence(text='x')])]
    stmts_out = fix_invalidities(stmts)
    assert len(stmts_out) == 1
    assert stmts_out[0].enz.db_refs == {'FPLX': 'ERK'}

    stmts_out = ac.fix_invalidities(stmts)

    assert len(stmts_out) == 1
    assert stmts_out[0].enz.db_refs == {'FPLX': 'ERK'}

    stmts_out = ac.fix_invalidities(stmts,
                                    in_place=True,
                                    print_report_before=True,
                                    print_report_after=True,
                                    prior_hash_annots=True)
    # Check the in-place effect
    assert stmts[1].enz.db_refs == {'FPLX': 'ERK'}
    assert stmts_out[0].enz.db_refs == {'FPLX': 'ERK'}


```
