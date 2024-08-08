# Description
Get the number of citations in PubMed for a search query.

# Code
```
import logging
import requests
import xml.etree.ElementTree as ET
from time import sleep
from functools import lru_cache

# Initialize logger
logger = logging.getLogger(__name__)

# Define the PubMed API URLs
pubmed_search = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'

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

def get_id_count(search_term):
    """Get the number of citations in Pubmed for a search query.

    Parameters
    ----------
    search_term : str
        A term for which the PubMed search should be performed.

    Returns
    -------
    int or None
        The number of citations for the query, or None if the query fails.
    """
    params = {'term': search_term,
              'rettype': 'count',
              'db': 'pubmed'}
    tree = send_request(pubmed_search, params)
    if tree is None:
        return None
    else:
        count = list(tree)[0].text

```
