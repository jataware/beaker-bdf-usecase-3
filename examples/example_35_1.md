# Description
Search PubMed for paper IDs given a search term with various configuration parameters, using lru_cache to optimize repeated identical searches.

# Code
```
import logging
import random
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

@lru_cache(maxsize=100)
def get_ids(search_term, **kwargs):
    """Search Pubmed for paper IDs given a search term.

    Search options can be passed as keyword arguments, some of which are
    custom keywords identified by this function, while others are passed on
    as parameters for the request to the PubMed web service
    For details on parameters that can be used in PubMed searches, see
    https://www.ncbi.nlm.nih.gov/books/NBK25499/#chapter4.ESearch Some useful
    parameters to pass are db='pmc' to search PMC instead of pubmed reldate=2
    to search for papers within the last 2 days mindate='2016/03/01',
    maxdate='2016/03/31' to search for papers in March 2016.

    PubMed, by default, limits returned PMIDs to a small number, and this
    number can be controlled by the "retmax" parameter. This function
    uses a retmax value of 10,000 by default (the maximum supported by PubMed)
    that can be changed via the corresponding keyword argument. Note also
    the retstart argument along with retmax to page across batches of IDs.

    PubMed's REST API makes it difficult to retrieve more than 10k
    PMIDs systematically. See the `get_all_ids` function in this module
    for a way to retrieve more than 10k IDs using the PubMed edirect CLI.

    Parameters
    ----------
    search_term : str
        A term for which the PubMed search should be performed.
    use_text_word : Optional[bool]
        If True, the "[tw]" string is appended to the search term to constrain
        the search to "text words", that is words that appear as whole
        in relevant parts of the PubMed entry (excl. for instance the journal
        name or publication date) like the title and abstract. Using this
        option can eliminate spurious search results such as all articles
        published in June for a search for the "JUN" gene, or journal names
        that contain Acad for a search for the "ACAD" gene.
        See also: https://www.nlm.nih.gov/bsd/disted/pubmedtutorial/020_760.html
        Default : True
    kwargs : kwargs
        Additional keyword arguments to pass to the PubMed search as
        parameters.
    """
    use_text_word = kwargs.pop('use_text_word', True)
    if use_text_word:
        search_term += '[tw]'
    params = {'term': search_term,
              'retmax': 10000,
              'retstart': 0,
              'db': 'pubmed',
              'sort': 'pub+date'}
    params.update(kwargs)
    tree = send_request(pubmed_search, params)
    if tree is None:
        return []
    if tree.find('ERROR') is not None:
        logger.error(tree.find('ERROR').text)
        return []
    if tree.find('ErrorList') is not None:
        for err in tree.find('ErrorList'):
            logger.error('Error - %s: %s' % (err.tag, err.text))
        return []
    count = int(tree.find('Count').text)
    id_terms = tree.findall('IdList/Id')
    if id_terms is None:
        return []
    ids = [idt.text for idt in id_terms]
    if count != len(ids):
        logger.warning('Not all ids were retrieved for search %s;\n'
                       'limited at %d.' % (search_term, params['retmax']))

```
