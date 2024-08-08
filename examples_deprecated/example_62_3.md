# Description
Test the extraction of agents from a protein family entity using INDRA BioPAX.

# Code
```
from indra.sources import biopax
import os
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'biopax_test.owl')

def test_protein_family_agent():
    bpe = bp.model.objects['Protein_da79d1a005a8eb259b0c09278ae9230e']
    agents = bp._get_agents_from_entity(bpe)
    assert len(agents) == 2
    assert {a.name for a in agents} == {'MAPK1', 'MAPK3'}

    mapk3 = agents[0]
    assert mapk3.name == 'MAPK3'
    assert len(mapk3.mods) == 2
    assert mapk3.mods[0].position == '202'
    assert mapk3.db_refs['UP'] == 'P27361', mapk3.db_refs

```
