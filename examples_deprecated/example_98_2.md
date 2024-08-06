# Description
Validate an invalid phosphorylation event using JSON schema and ensure it raises validation errors.

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
invalid_agent1 = {'name': 'RAS', 'db_refs': 2}
invalid_agent2 = {'db_refs': {'TEXT': 'RAS'}}
invalid_agent3 = {'name': 'cow', 'db_refs': {'TEXT': 'RAS'}, 'bound_conditions': 'mooooooooooo!'}

invalid_evidence = {'source_api': 42}

def val(s):

def test_invalid_phosphorylation():
    s = {'enz': valid_agent1, 'sub': valid_agent2, 'type': 'Phosphorylation',
         'id': '5', 'residue': 5}  # residue should be a string
    with pytest.raises(ValidationError):
        val(s)

    s = {'enz': valid_agent1, 'sub': invalid_agent1, 'type': 'Phosphorylation',
         'id': '5'}
    with pytest.raises(ValidationError):
        val(s)

    s = {'enz': valid_agent1, 'sub': invalid_agent2, 'type': 'Phosphorylation',
         'id': '5'}
    with pytest.raises(ValidationError):
        val(s)

    s = {'enz': valid_agent1, 'sub': invalid_agent3, 'type': 'Phosphorylation',
         'id': '5'}
    with pytest.raises(ValidationError):
        val(s)

    invalid_evidence = {'source_api': 42}
    s = {'enz': valid_agent1, 'sub': valid_agent2, 'type': 'Phosphorylation',

```
