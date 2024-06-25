# Description
Check article entitlement using the Elsevier API.

# Code
```
import os
import re
import logging
import textwrap
import datetime
import xml.etree.ElementTree as ET
import requests
from time import sleep
from indra.util import flatten
from indra import has_config, get_config
from functools import lru_cache, wraps
from indra.util import UnicodeXMLTreeBuilder as UTB

logger = logging.getLogger(__name__)

elsevier_api_url = 'https://api.elsevier.com/content'
elsevier_entitlement_url = '%s/article/entitlement/doi' % elsevier_api_url

ELSEVIER_KEYS = None
API_KEY_ENV_NAME = 'ELSEVIER_API_KEY'
INST_KEY_ENV_NAME = 'ELSEVIER_INST_KEY'


def _ensure_api_keys(task_desc, failure_ret=None):
    def check_func_wrapper(func):
        @wraps(func)
        def check_api_keys(*args, **kwargs):
            global ELSEVIER_KEYS
            if ELSEVIER_KEYS is None:
                ELSEVIER_KEYS = {}
                if not has_config(INST_KEY_ENV_NAME):
                    logger.warning('Institution API key %s not found in config '
                                   'file or environment variable: this will '
                                   'limit access for %s'
                                   % (INST_KEY_ENV_NAME, task_desc))
                ELSEVIER_KEYS['X-ELS-Insttoken'] = get_config(INST_KEY_ENV_NAME)
                if not has_config(API_KEY_ENV_NAME):
                    logger.error('API key %s not found in configuration file '
                                 'or environment variable: cannot %s'
                                 % (API_KEY_ENV_NAME, task_desc))
                    return failure_ret
                ELSEVIER_KEYS['X-ELS-APIKey'] = get_config(API_KEY_ENV_NAME)
            elif 'X-ELS-APIKey' not in ELSEVIER_KEYS.keys():
                logger.error('No Elsevier API key %s found: cannot %s'
                             % (API_KEY_ENV_NAME, task_desc))
                return failure_ret
            return func(*args, **kwargs)
        return check_api_keys

@_ensure_api_keys('check article entitlement', False)
def check_entitlement(doi):
    """Check whether IP and credentials enable access to content for a doi.

    This function uses the entitlement endpoint of the Elsevier API to check
    whether an article is available to a given institution. Note that this
    feature of the API is itself not available for all institution keys.
    """
    if doi.lower().startswith('doi:'):
        doi = doi[4:]
    url = '%s/%s' % (elsevier_entitlement_url, doi)
    params = {'httpAccept': 'text/xml'}
    res = requests.get(url, params, headers=ELSEVIER_KEYS)
    if not res.status_code == 200:
        logger.error('Could not check entitlements for article %s: '
                     'status code %d' % (doi, res.status_code))
        logger.error('Response content: %s' % res.text)
        return False

```
