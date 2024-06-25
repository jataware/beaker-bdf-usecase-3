# Description
A test for ensuring TEXT references are not removed during mapping.

# Code
```
from indra.preassembler.grounding_mapper import default_mapper as gm

def test_text_not_removed():
    agent = Agent('SERPINA1', db_refs={'UP': 'P01009', 'TEXT': 'PI',
                                       'HGNC': '8941', 'EGID': '5265'})
    mapped_agent = gm.map_agent(agent, do_rename=True)

```
