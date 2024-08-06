# Description
Creating and using a NestedDict, demonstrating recursive key assignment and path retrieval.

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

    >>> nd = NestedDict()
    >>> nd['a']['b']['c'] = 'foo'

    In addition, useful methods have been defined that allow the user to search
    the data structure. Note that the are not particularly optimized methods at
    this time. However, for convenience, you can for example simply call
    `get_path` to get the path to a particular key:

    >>> nd.get_path('c')

```
