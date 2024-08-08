# Description
Deserialize a JSON object into a BioContext instance.

# Code
```
import datetime

class Context(object):
    @classmethod
    def from_json(cls, jd):
        context_type = jd.get('type')
        if context_type == 'bio':
            return BioContext.from_json(jd)
        elif context_type == 'world':
            return WorldContext.from_json(jd)
        elif context_type == 'movement':
            return MovementContext.from_json(jd)
        else:
            raise ValueError('Unknown context type %s' % context_type)

class RefContext(object):
    @classmethod
    def from_json(cls, jd):

@classmethod
def from_json(cls, jd):
    # For all the attributes, we deserialize them if they have a value,
    # and make a dict that can be passed to the constructor
    ref_contexts = {attr: (RefContext.from_json(jd.get(attr))
                           if jd.get(attr) else None)
                    for attr in cls.attrs}
    bs = cls(**ref_contexts)

```
