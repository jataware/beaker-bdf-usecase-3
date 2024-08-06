# Description
Load the configuration file into a dictionary, converting keys to user-friendly format.

# Code
```
import os
import logging
if sys.version_info[0] == 3:
    from configparser import RawConfigParser
else:
    from ConfigParser import RawConfigParser

def populate_config_dict(config_path):
    """Load the configuration file into the config_file dictionary

    A ConfigParser-style configuration file can have multiple sections, but
    we ignore the section distinction  and load the key/value pairs from all
    sections into a single key/value list.
    """
    try:
        config_dict = {}
        parser = RawConfigParser()
        parser.optionxform = lambda x: x
        parser.read(config_path)
        sections = parser.sections()
        for section in sections:
            options = parser.options(section)
            for option in options:
                config_dict[option] = str(parser.get(section, option))
    except Exception as e:
        logger.warning("Could not load configuration file due to exception. "
                       "Only environment variable equivalents will be used.")
        return None

    for key in config_dict.keys():
        if config_dict[key] == '':
            config_dict[key] = None
        elif isinstance(config_dict[key], str):
            config_dict[key] = os.path.expanduser(config_dict[key])

```
