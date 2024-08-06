# Description
Example of standardizing agent names using GO identifier.

# Code
```
from indra.statements import Agent

def test_name_standardize_go():
    a1 = Agent('x', db_refs={'GO': 'GO:0006915'})
    standardize_agent_name(a1, False)

```
