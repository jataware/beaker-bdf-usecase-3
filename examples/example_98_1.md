# Description
Test and validate various types of modifications using JSON schema.

# Code
```
import json
import jsonschema
import os
import pytest
from jsonschema.exceptions import ValidationError

dir_this = os.path.dirname(__file__)
schema_file = os.path.join(dir_this, '../resources/statements_schema.json')
with open(schema_file, 'r') as f:
    schema = json.loads(f.read())

valid_agent1 = {'name': 'RAF', 'db_refs': {'TEXT': 'RAF'}}
valid_agent2 = {'name': 'RAS', 'db_refs': {'TEXT': 'RAS'}}
agent_mod = {'name': 'RAF', 'db_refs': {'TEXT': 'RAF'}, 'mods': [{'mod_type': 'phosphorylation', 'residue': 'S', 'position': '100', 'is_modified': True}]}
agent_mut = {'name': 'RAF', 'db_refs': {'TEXT': 'RAF'}, 'mutations': [{'position': '100', 'residue_from': 'S', 'residue_to': 'Y'}]}

def test_valid_modification():
    # Calls to validate() in this function should not raise exceptions
    mod_types = ['Phosphorylation', 'Dephosphorylation', 'Ubiquitination',
                 'Deubiquitination', 'Sumoylation', 'Desumoylation',
                 'Hydroxylation', 'Dehydroxylation', 'Acetylation',
                 'Deacetylation', 'Glycosylation', 'Deglycosylation',
                 'Farnesylation', 'Defarnesylation', 'Geranylgeranylation',
                 'Degeranylgeranylation', 'Palmitoylation', 'Depalmitoylation',
                 'Myristoylation', 'Demyristoylation', 'Ribosylation',
                 'Deribosylation', 'Methylation', 'Demethylation',
                 'Activation', 'Inhibition', 'IncreaseAmount',
                 'DecreaseAmount']

    for mod_type in mod_types:
        s = {'enz': valid_agent1, 'sub': valid_agent2,
             'type': mod_type, 'id': '5'}
        jsonschema.validate([s], schema)

        s['enz'] = agent_mod
        jsonschema.validate([s], schema)

        s['enz'] = agent_mut
        jsonschema.validate([s], schema)

        s['enz'] = agent_act
        jsonschema.validate([s], schema)

        if mod_type not in ['Activation', 'Inhibition', 'IncreaseAmount',
                            'DecreaseAmount']:
            s['residue'] = 'S'
            jsonschema.validate([s], schema)

            s['position'] = '10'

```
