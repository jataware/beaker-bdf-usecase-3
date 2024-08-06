# Description
Example of standardizing agent names and converting between databases.

# Code
```
from indra.statements import Agent

def test_name_standardize_mesh_other_db():
    a1 = Agent('x', db_refs={'MESH': 'D001194'})
    standardize_agent_name(a1, True)
    assert a1.db_refs['CHEBI'] == 'CHEBI:46661'
    assert a1.name == 'asbestos', a1.name

    db_refs = {'MESH': 'D000067777'}
    db_refs = standardize_db_refs(db_refs)
    assert db_refs.get('HGNC') == '3313', db_refs
    assert db_refs.get('UP') == 'Q12926', db_refs
    a2 = Agent('x', db_refs=db_refs)
    standardize_agent_name(a2)

```
