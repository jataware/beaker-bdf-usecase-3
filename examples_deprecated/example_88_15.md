# Description
A test for handling mismatched HGNC and UP IDs.

# Code
```
indra.preassembler.grounding_mapper import GroundingMapper
indra.statements import Agent, Phosphorylation

def test_up_and_invalid_hgnc_sym():
    erk = Agent('ERK1', db_refs={'TEXT': 'ERK1'})
    stmt = Phosphorylation(None, erk)
    g_map = {'ERK1': {'TEXT': 'ERK1', 'UP': 'P28482', 'HGNC': 'foobar'}}
    with pytest.raises(ValueError):

```
