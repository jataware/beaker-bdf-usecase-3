# Description
Test and validate a valid event using JSON schema.

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

valid_concept1 = {'name': 'government', 'db_refs': {'TEXT': 'government'}}

def test_valid_event():

```
