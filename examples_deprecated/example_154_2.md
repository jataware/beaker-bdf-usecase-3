# Description
Retrieving a key and its value from a NestedDict structure.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str

class NestedDict(dict):
    def __getitem__(self, key):
        if key not in self.keys():
            val = self.__class__()
            self.__setitem__(key, val)
        else:
            val = dict.__getitem__(self, key)
        return val

    def get_path(self, key):
        if key in self.keys():
            return (key,), self[key]
        else:
            key_path, res = (None, None)
            for sub_key, v in self.items():
                if isinstance(v, self.__class__):
                    key_path, res = v.get_path(key)
                elif hasattr(v, 'get'):
                    res = v.get(key)
                    key_path = (key,) if res is not None else None
                if res is not None and key_path is not None:
                    key_path = (sub_key,) + key_path
                    break

>>> nd.get_path('b')
(('a', 'b'), NestedDict(
  'c': 'foo'

```
