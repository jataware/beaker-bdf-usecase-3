# Description
Extracting an agent from grounding string using 'get_agent_from_grounding' function and validating its properties.

# Code
```

def test_get_agent_from_grounding():
    ag = get_agent_from_grounding('uniprotkb:P15056')
    assert ag.name == 'BRAF'
    assert ag.db_refs['UP'] == 'P15056', ag.db_refs

    ag = get_agent_from_grounding('uniprotkb:P15056-PRO_0000085665')
    # This is the name of the chain in UniProt which takes precedence
    # if we have a feature ID
    assert ag.name == 'Serine/threonine-protein kinase B-raf'
    assert ag.db_refs['UP'] == 'P15056'
    assert ag.db_refs['UPPRO'] == 'PRO_0000085665'

    ag = get_agent_from_grounding('refseq:NP_828867')

```
