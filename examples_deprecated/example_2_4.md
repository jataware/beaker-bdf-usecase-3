# Description
Check if the configuration value for the given key is present.

# Code
```
import os
import logging
if sys.version_info[0] == 3:
    from configparser import RawConfigParser
else:
    from ConfigParser import RawConfigParser
class IndraConfigError(Exception):
    pass
CONFIG_DICT = {
    'key1': 'value1',
    'key2': 'value2'

def has_config(key):
    """Returns whether the configuration value for the given kehy is present.

    Parameters
    ----------
    key : str
        The key for the configuration value to fetch

    Returns
    -------
    value : bool
        Whether the configuration value is present
    """

```
