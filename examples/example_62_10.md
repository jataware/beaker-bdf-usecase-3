# Description
Test the creation of a standard agent using INDRA BioPAX processor's get_standard_agent function.

# Code
```

def test_valid_agent():
    agent = bpc.get_standard_agent('x', {'HGNC': '1097', 'EGID': '---'})
    assert agent.name == 'BRAF'
    assert agent.db_refs.get('EGID') != '---'

```
