# Description
Validate various invalid complex statements using JSON schema and ensure they raise validation errors.

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
valid_agent2 = {'name': 'RAS', 'db_refs': {'TEXT': 'RAS'}}

def val(s):

def test_invalid_complex():
    s = {'members': [invalid_agent1, valid_agent2], 'type': 'Complex',
         'id': '3'}
    with pytest.raises(ValidationError):
        val(s)

    s = {'members': [valid_agent1, invalid_agent2], 'type': 'Complex',
         'id': '3'}
    with pytest.raises(ValidationError):

```
