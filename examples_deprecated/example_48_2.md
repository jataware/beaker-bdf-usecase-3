# Description
Deserialize a JSON dictionary to create a Concept object.

# Code
```
import logging
from collections import OrderedDict as _o

logger = logging.getLogger(__name__)

class Concept(object):
    def __init__(self, name, db_refs=None):
        self.name = name
        self.db_refs = db_refs if db_refs else {}
    def to_json(self):
        json_dict = _o({'name': self.name})
        json_dict['db_refs'] = self.db_refs
        return json_dict
    @classmethod
    def _from_json(cls, json_dict):
        name = json_dict.get('name')
        db_refs = json_dict.get('db_refs', {})
        if not name:
            logger.error('Concept missing name.')
            return None
        for key, val in db_refs.items():
            if isinstance(val, list):
                db_refs[key] = [tuple(v) for v in val]
        concept = Concept(name, db_refs=db_refs)

@classmethod
def _from_json(cls, json_dict):
    name = json_dict.get('name')
    db_refs = json_dict.get('db_refs', {})
    if not name:
        logger.error('Concept missing name.')
        return None
    # This fixes the fact that scored lists of groundings
    # are deserialized as lists of lists instead of lists
    # of tuples.
    for key, val in db_refs.items():
        if isinstance(val, list):
            db_refs[key] = [tuple(v) for v in val]
    concept = Concept(name, db_refs=db_refs)

```
