# Description
Test and validate various self-modification statements using JSON schema.

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


def test_self_modifications():
    self_mods = ['Autophosphorylation', 'Transphosphorylation']
    for self_mod in self_mods:
        s = {'type': self_mod, 'id': '20', 'enz': valid_agent1}
        jsonschema.validate([s], schema)

        s['residue'] = 'S'
        jsonschema.validate([s], schema)

        s['position'] = '10'

```
