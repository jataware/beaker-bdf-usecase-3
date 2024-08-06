# Description
Example of standardizing agent names using UP and UPPRO identifiers.

# Code
```
from indra.statements import Agent

def test_standardize_uppro():
    ag = Agent('x', db_refs={'UP': 'P01019'})
    standardize_agent_name(ag)
    assert ag.name == 'AGT'
    ag = Agent('x', db_refs={'UPPRO': 'PRO_0000032458'})
    standardize_agent_name(ag)
    assert ag.name == 'Angiotensin-2', ag.name
    ag = Agent('x', db_refs={'UPPRO': 'PRO_0000032458', 'UP': 'P01019'})
    standardize_agent_name(ag)

```
