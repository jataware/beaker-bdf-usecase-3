# Description
Return PMIDs that are annotated with a given MeSH ID using an optional major_topic flag.

# Code
```
import logging
import requests
import xml.etree.ElementTree as ET
from functools import lru_cache
from typing import List

# Initialize logger
logger = logging.getLogger(__name__)

# Define the PubMed API URLs
pubmed_search = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'

# Stub for import from indra.databases
from indra.databases import mesh_client

# Define send_request function

def send_request(url, data, retry_pause=1, max_tries=3):
    try:
        res = requests.get(url, params=data)
    except requests.exceptions.Timeout as e:
        logger.error('PubMed request timed out')
        logger.error('url: %s, data: %s' % (url, data))
        logger.error(e)
        return None
    except requests.exceptions.RequestException as e:
        logger.error('PubMed request exception')
        logger.error('url: %s, data: %s' % (url, data))
        logger.error(e)
        return None
    if res.status_code in {400, 429, 502, 503} and max_tries > 0:
        sleep(retry_pause)
        retry_pause += 0.5 + 1.5 * random.random()
        return send_request(url, data, retry_pause, max_tries - 1)
    if not res.status_code == 200:
        logger.error('Got return code %d from pubmed client.' % res.status_code)
        return None
    tree = ET.XML(res.content)

def get_ids_for_mesh(mesh_id, major_topic=False, **kwargs):
    """Return PMIDs that are annotated with a given MeSH ID.

    Parameters
    ----------
    mesh_id : str
        The MeSH ID of a term to search for, e.g., D009101.
    major_topic : bool
        If True, only papers for which the given MeSH ID is annotated as
        a major topic are returned. Otherwise all annotations are considered.
        Default: False
    **kwargs
        Any further PudMed search arguments that are passed to
        get_ids.
    """
    from indra.databases import mesh_client
    mesh_name = mesh_client.get_mesh_name(mesh_id)
    if not mesh_name:
        logger.error('Could not get MeSH name for ID %s' % mesh_id)
        return []
    suffix = 'majr' if major_topic else 'mh'
    search_term = '%s [%s]' % (mesh_name, suffix)
    ids = get_ids(search_term, use_text_word=False, **kwargs)
    if mesh_id.startswith('C') and not major_topic:
        # Get pmids for supplementary concepts as well
        search_term = '%s [nm]' % mesh_name
        ids2 = get_ids(search_term, use_text_word=False, **kwargs)
        ids = list(set(ids) | set(ids2))

```
