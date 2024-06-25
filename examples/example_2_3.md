# Description
Get a value by key from the config file or environment.

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

def get_config(key, failure_ok=True):
    """Get value by key from config file or environment.

    Returns the configuration value, first checking the environment
    variables and then, if it's not present there, checking the configuration
    file.

    Parameters
    ----------
    key : str
        The key for the configuration value to fetch
    failure_ok : Optional[bool]
        If False and the configuration is missing, an IndraConfigError is
        raised. If True, None is returned and no error is raised in case
        of a missing configuration. Default: True

    Returns
    -------
    value : str or None
        The configuration value or None if the configuration value doesn't
        exist and failure_ok is set to True.
    """
    err_msg = "Key %s not in environment or config file." % key
    if key in os.environ:
        return os.environ[key]
    elif key in CONFIG_DICT:
        val = CONFIG_DICT[key]
        # We interpret an empty value in the config file as a failure
        if val is None and not failure_ok:
            msg = 'Key %s is set to an empty value in config file.' % key
            raise IndraConfigError(msg)
        else:
            return val
    elif not failure_ok:
        raise IndraConfigError(err_msg)
    else:

```
