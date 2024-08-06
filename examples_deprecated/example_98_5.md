# Description
Test and validate a valid complex statement using JSON schema.

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

def test_valid_complex():
    s = {'members': [valid_agent1, valid_agent2], 'type': 'Complex', 'id': '3'}
    jsonschema.validate([s], schema)

    s = {'members': [], 'type': 'Complex', 'id': '3'}

```
