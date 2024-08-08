# Description
Example of standardizing agent names using MESH identifier.

# Code
```
from indra.statements import Agent

def test_name_standardize_mesh():
    a1 = Agent('x', db_refs={'MESH': 'D008545'})
    standardize_agent_name(a1, False)

```
