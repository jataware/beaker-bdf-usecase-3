# Description
Test and validate a GEF statement using JSON schema.

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

def test_gef():
    s = {'type': 'Gef', 'id': '40', 'gef': valid_agent1, 'ras': valid_agent2}

```
