# Description
Example of standardizing agent names using CHEBI identifier.

# Code
```
from indra.statements import Agent

def test_name_standardize_chebi():
    a1 = Agent('x', db_refs={'CHEBI': 'CHEBI:15996'})
    standardize_agent_name(a1, False)

```
