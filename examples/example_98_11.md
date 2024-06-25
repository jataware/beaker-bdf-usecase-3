# Description
Validate various invalid conversion statements using JSON schema and ensure they raise validation errors.

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
valid_agent3 = {'name': 'ERK', 'db_refs': {'TEXT': 'ERK'}}

def val(s):

def test_invalid_conversion():
    s = {'type': 'Conversion', 'id': '11', 'subj': valid_agent1,
         'obj_from': [12, valid_agent3], 'obj_to': [valid_agent3]}
    with pytest.raises(ValidationError):
        val(s)

    s = {'type': 'Conversion', 'id': '11', 'subj': valid_agent1,
         'obj_from': [valid_agent2, valid_agent3],
         'obj_to': [valid_agent3, 12]}
    with pytest.raises(ValidationError):
        val(s)

    s = {'type': 'Conversion', 'id': '11', 'subj': 'dog',
         'obj_from': [valid_agent2, valid_agent3], 'obj_to': [valid_agent3]}
    with pytest.raises(ValidationError):
        val(s)

    s = {'type': 'Conversion', 'id': '11', 'subj': valid_agent1,
         'obj_from': 'banana', 'obj_to': [valid_agent3]}
    with pytest.raises(ValidationError):

```
