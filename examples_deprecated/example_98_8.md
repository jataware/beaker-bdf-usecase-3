# Description
Test and validate a valid influence statement using JSON schema.

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
valid_concept2 = {'name': 'agriculture', 'db_refs': {'TEXT': 'agriculture'}}
valid_event1 = {'type': 'Event', 'concept': valid_concept1, 'id': '2'}

def test_valid_influence():
    s = {'subj': valid_event1, 'obj': valid_event2, 'subj_delta': None,
         'obj_delta': None, 'type': 'Influence', 'id': '10'}

```
