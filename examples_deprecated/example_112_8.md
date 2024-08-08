# Description
Example of standardizing agent names using EFO, HP, and DOID identifiers and mapping to MESH.

# Code
```
from indra.statements import Agent

def test_standardize_name_efo_hp_doid():
    ag = Agent('x', db_refs={'HP': 'HP:0031801'})
    standardize_agent_name(ag)
    # Name based on MESH mapping
    assert ag.name == 'Vocal Cord Dysfunction'

    ag = Agent('x', db_refs={'HP': 'HP:0000002'})
    standardize_agent_name(ag)
    # Name based on HP itself
    assert ag.name == 'Abnormality of body height'

    ag = Agent('x', db_refs={'DOID': 'DOID:0014667'})
    standardize_agent_name(ag)
    # Name based on MESH mapping
    assert ag.name == 'Metabolic Diseases'

    ag = Agent('x', db_refs={'EFO': '1002050'})
    standardize_agent_name(ag)
    # Name based on MESH mapping
    assert ag.name == 'Nephritis', (ag.name, ag.db_refs)

    ag = Agent('x', db_refs={'EFO': '0000001'})
    standardize_agent_name(ag)
    # Name based on EFO itself

```
