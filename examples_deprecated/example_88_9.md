# Description
A test for renaming agents based on different reference sources.

# Code
```
from indra.preassembler.grounding_mapper import default_mapper as gm

def test_renaming():
    akt_indra = Agent('pkbA', db_refs={'TEXT': 'Akt', 'FPLX': 'AKT',
                                       'UP': 'P31749'})
    akt_hgnc_from_up = Agent('pkbA', db_refs={'TEXT': 'Akt', 'UP': 'P31749'})
    akt_other = Agent('pkbA', db_refs={'TEXT': 'Akt'})
    tat_up_no_hgnc = Agent('foo', db_refs={'TEXT': 'bar', 'UP': 'P04608'})
    stmts = [Phosphorylation(None, akt_indra),
             Phosphorylation(None, akt_hgnc_from_up),
             Phosphorylation(None, akt_other),
             Phosphorylation(None, tat_up_no_hgnc), ]
    renamed_stmts = gm.rename_agents(stmts)
    assert len(renamed_stmts) == 4
    # Should draw on BE first
    assert renamed_stmts[0].sub.name == 'AKT'
    # Then on the HGNC lookup from Uniprot
    assert renamed_stmts[1].sub.name == 'AKT1', renamed_stmts[1].sub.name
    # Don't fall back on text if there's no grounding
    assert renamed_stmts[2].sub.name == 'pkbA'

```
