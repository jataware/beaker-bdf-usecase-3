# Description
Validate various invalid influence statements using JSON schema and ensure they raise validation errors.

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
invalid_concept1 = {'name': 3, 'db_refs': {'TEXT': 'government'}}
invalid_concept2 = {'name': 'government'}

def val(s):

def test_invalid_influence():
    s = {'subj': invalid_concept1, 'obj': valid_concept2, 'subj_delta': None,
         'obj_delta': None, 'type': 'Influence', 'id': '10'}
    with pytest.raises(ValidationError):
        val(s)

    s = {'subj': valid_concept1, 'obj': invalid_concept2, 'subj_delta': None,
         'obj_delta': None, 'type': 'Influence', 'id': '10'}
    with pytest.raises(ValidationError):
        val(s)

    s = {'subj': valid_concept1, 'obj': valid_concept2, 'subj_delta': None,
         'obj_delta': 'Henry', 'type': 'Influence', 'id': '10'}
    with pytest.raises(ValidationError):
        val(s)

    s = {'subj': valid_concept1, 'obj': valid_concept2, 'subj_delta': 'Larry',
         'obj_delta': None, 'type': 'Influence', 'id': '10'}
    with pytest.raises(ValidationError):
        val(s)

    s = {'subj': valid_concept1, 'obj': valid_concept2, 'subj_delta': None,
         'obj_delta': None, 'type': 'Influence', 'id': 10}
    with pytest.raises(ValidationError):

```
