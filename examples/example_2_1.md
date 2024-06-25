# Description
Create a configuration file from a default if it doesn't exist.

# Code
```
import os
import shutil
import logging
if sys.version_info[0] == 3:
    from configparser import RawConfigParser
else:
    from ConfigParser import RawConfigParser
logger = logging.getLogger(__name__)
home_dir = os.path.expanduser('~')
config_dir = os.path.join(home_dir, '.config', 'indra')
config_path = os.path.join(config_dir, 'config.ini')

if not os.path.isfile(config_path):
    try:
        os.makedirs(config_dir)
    except Exception:
        logger.warning(config_dir + ' already exists')
    try:
        shutil.copyfile(default_config_path, config_path)
    except Exception:

```
