# Description
Test and validate a translocation statement using JSON schema and check for validation error cases.

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


def test_translocation():
    s = {'type': 'Translocation', 'id': '30', 'agent': valid_agent1}
    jsonschema.validate([s], schema)

    s['from_location'] = 'A'
    jsonschema.validate([s], schema)

    s['to_location'] = 'B'
    jsonschema.validate([s], schema)

    s['to_location'] = 3
    with pytest.raises(ValidationError):

```
