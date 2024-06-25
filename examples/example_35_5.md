# Description
Get the full XML tree of a single article from the PubMed database, optionally saving it to a file.

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
pubmed_fetch = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'

# Stub for pretty_save_xml function
from indra.util import pretty_save_xml

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

@lru_cache(maxsize=100)
def get_full_xml(pubmed_id, fname=None):
    """Get the full XML tree of a single article from the Pubmed database.

    Parameters
    ----------
    pubmed_id : str
        A PubMed ID.
    fname : Optional[str]
        If given, the XML is saved to the given file name.

    Returns
    -------
    xml.etree.ElementTree.Element
        The root element of the XML tree representing the PubMed entry.
        The root is a PubmedArticleSet with a single PubmedArticle element
        that contains the article metadata.
    """
    if pubmed_id.upper().startswith('PMID'):
        pubmed_id = pubmed_id[4:]
    params = {'db': 'pubmed',
              'retmode': 'xml',
              'id': pubmed_id}
    tree = send_request(pubmed_fetch, params)
    if fname:
        pretty_save_xml(tree, fname)

```
