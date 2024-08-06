# Description
Convert MovementContext to a JSON serializable dictionary.

# Code
```
class MovementContext(Context):
    def __init__(self, locations=None, time=None):
        self.locations = locations if locations else []
        self.time = time

    @classmethod
    def from_json(cls, jd):
        locations_entry = jd.get('locations')
        if locations_entry:
            locations = [
                {'location': RefContext.from_json(location['location']),
                 'role': location['role']} for location in locations_entry]
        else:
            locations = None
        time_entry = jd.get('time')
        if time_entry:
            time = TimeContext.from_json(time_entry)
        else:
            time = None

def to_json(self):
    if self.locations:
        locations_json = [
            {'location': location['location'].to_json(),
             'role': location['role']} for location in self.locations]
    else:
        locations_json = []
    jd = {'type': 'movement',
          'locations': locations_json,
          'time': self.time.to_json() if self.time else None}

```
