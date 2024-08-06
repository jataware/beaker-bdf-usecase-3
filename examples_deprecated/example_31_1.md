# Description
Defines a function to get the metadata of an article given its DOI using CrossRef API.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
import os
import logging
import requests
from indra.config import get_config
from indra.literature import pubmed_client
try:
    from functools import lru_cache
except ImportError:
    from functools32 import lru_cache

logger = logging.getLogger(__name__)

@lru_cache(maxsize=100)
def get_metadata(doi):
    """Returns the metadata of an article given its DOI from CrossRef
    as a JSON dict"""
    url = crossref_url + 'works/' + doi
    res = requests.get(url)
    if res.status_code != 200:
        logger.info('Could not get CrossRef metadata for DOI %s, code %d' %
                    (doi, res.status_code))
        return None
    raw_message = res.json()
    metadata = raw_message.get('message')

```
