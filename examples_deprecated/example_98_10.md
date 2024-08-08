# Description
Test and validate a valid conversion statement using JSON schema.

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

def test_valid_conversion():
    s = {'type': 'Conversion', 'id': '11', 'subj': valid_agent1,
         'obj_from': [valid_agent2, valid_agent3], 'obj_to': [valid_agent3]}

```
