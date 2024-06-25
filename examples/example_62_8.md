# Description
Test the extraction of ChEBI grounding from a small molecule entity in a BioPAX file using INDRA.

# Code
```
from indra.sources import biopax
import os
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'biopax_test.owl')

def test_chebi_grounding_extraction():
    bpe = 'SmallMolecule_49d78305d95647ad81961ec7f6189821'
    sm = bp.model.objects[bpe]
    agents = bp._get_agents_from_singular_entity(sm)
    assert len(agents) == 1
    assert agents[0].name == 'GTP'

```
