# Description
Initialize and cache the INDRA bio ontology.

# Code
```
import os
import pickle
import logging
from indra.config import get_config

def initialize(self, rebuild=False):
    if rebuild or not os.path.exists(CACHE_FILE):
        logger.info('Initializing INDRA bio ontology for the first time, '
                    'this may take a few minutes...')
        self._build()
        # Try to create the folder first, if it fails, we don't cache
        if not os.path.exists(CACHE_DIR):
            try:
                os.makedirs(CACHE_DIR)
            except Exception:
                logger.warning('%s could not be created.' % CACHE_DIR)
        # Try to dump the file next, if it fails, we don't cache
        try:
            logger.info('Caching INDRA bio ontology at %s' % CACHE_FILE)
            with open(CACHE_FILE, 'wb') as fh:
                pickle.dump(self, fh, pickle.HIGHEST_PROTOCOL)
        except Exception:
            logger.warning('Failed to cache ontology at %s.' % CACHE_FILE)
    else:
        logger.info(
            'Loading INDRA bio ontology from cache at %s' % CACHE_FILE)
        with open(CACHE_FILE, 'rb') as fh:

```
