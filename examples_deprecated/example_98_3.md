# Description
Test and validate a valid active form using JSON schema.

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


def test_valid_active_form():
    s = {'agent': valid_agent1, 'activity': 'kinase', 'is_active': True,
         'type': 'ActiveForm', 'id': '6'}

```
