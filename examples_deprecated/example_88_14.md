# Description
A test for handling invalid HGNC IDs.

# Code
```
indra.preassembler.grounding_mapper import default_mapper as gm
indra.statements import Agent, Phosphorylation

def test_hgnc_sym_with_no_id():
    erk = Agent('ERK1', db_refs={'TEXT': 'ERK1'})
    stmt = Phosphorylation(None, erk)
    g_map = {'ERK1': {'TEXT': 'ERK1', 'HGNC': 'foobar'}}
    with pytest.raises(ValueError):
        gm = GroundingMapper(g_map)

```
