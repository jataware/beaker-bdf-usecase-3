# Description
Convert WorldContext to a JSON serializable dictionary.

# Code
```
class WorldContext(Context):
    def __init__(self, time=None, geo_location=None):
        self.time = time
        self.geo_location = geo_location

    @classmethod
    def from_json(cls, jd):
        time_entry = jd.get('time')
        time = TimeContext.from_json(time_entry) if time_entry else None
        geo_entry = jd.get('geo_location')
        geo_location = RefContext.from_json(geo_entry) if geo_entry else None

def to_json(self):
    jd = {'type': 'world',
          'time': self.time.to_json() if self.time else None,
          'geo_location': (self.geo_location.to_json()
                           if self.geo_location else None)}

```
