# Description
Test the `process_json_bio_entities` function from the `indra.sources.eidos` library to ensure it extracts biological entities from Eidos JSON correctly.

# Code
```
import os
import json
from indra.sources import eidos
from indra.statements import Agent


def test_bio_entity_extract():
    jsonld = os.path.join(path_this, 'eidos_bio_abstract.json')
    with open(jsonld, 'r') as fh:
        js = json.load(fh)
    agents = eidos.process_json_bio_entities(js)
    assert len(agents) == 11, agents
    from indra.statements import Agent
    assert all(isinstance(a, Agent) for a in agents)
    ag = [a for a in agents if a.name == 'Therapeutics'][0]

```
