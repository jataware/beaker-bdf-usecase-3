# Description
Convert WorldContext from a JSON object.

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

class TimeContext(object):
    @classmethod
    def from_json(cls, jd):
        return cls(text=jd.get('text'),
                   start=datetime.datetime.strptime(jd.get('start'), '%Y-%m-%dT%H:%M') if jd.get('start') else None,
                   end=datetime.datetime.strptime(jd.get('end'), '%Y-%m-%dT%H:%M') if jd.get('end') else None,
                   duration=jd.get('duration'))

class RefContext(object):
    @classmethod
    def from_json(cls, jd):

@classmethod
def from_json(cls, jd):
    time_entry = jd.get('time')
    time = TimeContext.from_json(time_entry) if time_entry else None
    geo_entry = jd.get('geo_location')
    geo_location = RefContext.from_json(geo_entry) if geo_entry else None

```
