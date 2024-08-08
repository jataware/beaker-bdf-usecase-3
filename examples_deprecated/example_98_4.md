# Description
Validate various invalid active forms using JSON schema and ensure they raise validation errors.

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

invalid_agent1 = {'name': 'RAS', 'db_refs': 2}
valid_agent1 = {'name': 'RAF', 'db_refs': {'TEXT': 'RAF'}}

def val(s):

def test_invalid_active_form():
    s = {'agent': invalid_agent1, 'activity': 'kinase', 'is_active': True,
         'type': 'ActiveForm', 'id': '6'}
    with pytest.raises(ValidationError):
        val(s)

    s = {'agent': valid_agent1, 'activity': 'kinase', 'is_active': 'moo',
         'type': 'ActiveForm', 'id': '6'}
    with pytest.raises(ValidationError):
        val(s)

    s = {'agent': valid_agent1, 'activity': 'kinase', 'is_active': True,
         'type': 'ActiveForm', 'id': 42}
    with pytest.raises(ValidationError):
        val(s)

    s = {'agent': valid_agent1, 'activity': 'kinase', 'is_active': True,
         'type': 'MOO', 'id': '6'}
    with pytest.raises(ValidationError):
        val(s)

    s = {'agent': valid_agent1, 'activity': {'cow': False}, 'is_active': True,
         'type': 'ActiveForm', 'id': '6'}
    with pytest.raises(ValidationError):

```
