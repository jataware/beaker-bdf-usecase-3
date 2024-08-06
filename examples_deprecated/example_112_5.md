# Description
Example of standardizing agent names using both MESH and GO identifiers.

# Code
```
from indra.statements import Agent

def test_name_standardize_mesh_go():
    a1 = Agent('x', db_refs={'MESH': 'D058750'})
    standardize_agent_name(a1, True)
    assert a1.db_refs['GO'] == 'GO:0001837'
    assert a1.name == 'epithelial to mesenchymal transition', a1.name
    a1 = Agent('x', db_refs={'GO': 'GO:0001837'})
    standardize_agent_name(a1, True)
    assert a1.db_refs['MESH'] == 'D058750'

```
