# Description
Example of standardizing agent names using HGNC, UP, and other identifiers.

# Code
```
from indra.statements import Agent

def test_name_standardize_hgnc_up():
    a1 = Agent('x', db_refs={'HGNC': '9387'})
    standardize_agent_name(a1, True)
    assert a1.name == 'PRKAG3'
    a1 = Agent('x', db_refs={'UP': 'Q9UGI9'})
    standardize_agent_name(a1, True)
    assert a1.name == 'PRKAG3'
    a1 = Agent('x', db_refs={'UP': 'Q8BGM7'})
    standardize_agent_name(a1, True)

```
