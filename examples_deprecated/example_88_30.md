# Description
A test for grounding with both TEXT and TEXT_NORM references.

# Code
```
from indra.statements import Agent, Phosphorylation, Evidence

def test_text_and_norm_text():
    gm.gilda_mode = 'local'

    # We should filter out ignores in both TEXT and TEXT_NORM
    ag = Agent('x', db_refs={'TEXT': 'XREF_BIBR', 'TEXT_NORM': 'ERK'})
    stmt = Phosphorylation(None, ag)
    res = gm.map_stmts([stmt])
    assert not res
    ag = Agent('x', db_refs={'TEXT': 'ERK', 'TEXT_NORM': 'XREF_BIBR'})
    stmt = Phosphorylation(None, ag)
    res = gm.map_stmts([stmt])
    assert not res

    # We should disambiguate based on both TEXT and TEXT_NORM
    ag = Agent('x', db_refs={'TEXT': 'AA', 'TEXT_NORM': 'XXX'},)
    stmt = Phosphorylation(None, ag,
                           evidence=Evidence(text='Arachidonic acid (AA)'))
    res = gm.map_stmts([stmt])
    assert res[0].sub.name == 'arachidonic acid', res[0]
    ag = Agent('x', db_refs={'TEXT': 'XXX', 'TEXT_NORM': 'AA'})
    stmt = Phosphorylation(None, ag,
                           evidence=Evidence(text='Arachidonic acid (AA)'))
    res = gm.map_stmts([stmt])
    assert res[0].sub.name == 'arachidonic acid', res[0]

    ag = Agent('x', db_refs={'TEXT': 'XXX', 'TEXT_NORM': 'ERK'})
    stmt = Phosphorylation(None, ag)
    res = gm.map_stmts([stmt])
    assert res[0].sub.name == 'ERK', res[0]

    ag = Agent('x', db_refs={'TEXT': 'ERK', 'TEXT_NORM': 'XXX'})
    stmt = Phosphorylation(None, ag)
    res = gm.map_stmts([stmt])

```
