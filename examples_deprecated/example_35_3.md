# Description
Get the curated set of articles for a gene in the Entrez database by HGNC name.

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

# Stub for import from indra.databases
from indra.databases import hgnc_client

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
def get_ids_for_gene(hgnc_name, **kwargs):
    """Get the curated set of articles for a gene in the Entrez database.

    Search parameters for the Gene database query can be passed in as
    keyword arguments.

    Parameters
    ----------
    hgnc_name : str
        The HGNC name of the gene. This is used to obtain the HGNC ID
        (using the hgnc_client module) and in turn used to obtain the Entrez
        ID associated with the gene. Entrez is then queried for that ID.
    """
    from indra.databases import hgnc_client
    # Get the HGNC ID for the HGNC name
    hgnc_id = hgnc_client.get_hgnc_id(hgnc_name)
    if hgnc_id is None:
        raise ValueError('Invalid HGNC name.')
    # Get the Entrez ID
    entrez_id = hgnc_client.get_entrez_id(hgnc_id)
    if entrez_id is None:
        raise ValueError('Entrez ID not found in HGNC table.')
    # Query the Entrez Gene database
    params = {'db': 'gene',
              'retmode': 'xml',
              'id': entrez_id}
    params.update(kwargs)
    tree = send_request(pubmed_fetch, params)
    if tree is None:
        return []
    if tree.find('ERROR') is not None:
        logger.error(tree.find('ERROR').text)
        return []
    # Get all PMIDs from the XML tree
    id_terms = tree.findall('.//PubMedId')
    if id_terms is None:
        return []
    # Use a set to remove duplicate IDs
    ids = list(set([idt.text for idt in id_terms]))

```
