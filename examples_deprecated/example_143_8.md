# Description
Getting UPPRO name from grounding string using 'get_agent_from_grounding' function and validating its properties.

# Code
```

def test_get_uppro_name():
    ag = get_agent_from_grounding('uniprotkb:Q32ZE1-PRO_0000435839')
    assert ag.db_refs['UP'] == 'Q32ZE1'
    assert ag.db_refs['UPPRO'] == 'PRO_0000435839'

```
