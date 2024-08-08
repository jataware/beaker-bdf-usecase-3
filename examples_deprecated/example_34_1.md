# Description
Example code demonstrating how to look up a paper ID to get corresponding PMID, DOI, and PMCID.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
import re
import logging
import os.path
import requests
from lxml import etree
from lxml.etree import QName
import xml.etree.ElementTree as ET
from indra.literature import pubmed_client
from indra.util import UnicodeXMLTreeBuilder as UTB

# Python 2
try:
    basestring
# Python 3
except:
    basestring = str

logger = logging.getLogger(__name__)
pmc_url = 'https://www.ncbi.nlm.nih.gov/pmc/oai/oai.cgi'

def id_lookup(paper_id, idtype=None):
    """Return PMID, DOI and PMCID based on an input ID.

    This function takes a Pubmed ID, Pubmed Central ID, or DOI
    and use the Pubmed ID mapping service and looks up all other IDs from one
    of these. The IDs are returned in a dictionary.

    Parameters
    ----------
    paper_id : str
        A PubMed ID, PubMed Central ID, or DOI.
    idtype : Optional[str]
        The type of the input ID. If not given, the function will try to
        determine the type from the input ID. If given, it must be one of
        'pmid', 'pmcid', or 'doi'.

    Returns
    -------
    dict
        A dictionary with keys 'pmid', 'pmcid', and 'doi' containing the
        corresponding IDs, or an empty dict if lookup fails.
    """
    if idtype is not None and idtype not in ('pmid', 'pmcid', 'doi'):
        raise ValueError("Invalid idtype %s; must be 'pmid', 'pmcid', "
                         "or 'doi'." % idtype)
    if paper_id.upper().startswith('PMC'):
        idtype = 'pmcid'
    # Strip off any prefix
    if paper_id.upper().startswith('PMID'):
        paper_id = paper_id[4:]
    elif paper_id.upper().startswith('DOI'):
        paper_id = paper_id[3:]
    data = {'ids': paper_id}
    if idtype is not None:
        data['idtype'] = idtype
    try:
        tree = pubmed_client.send_request(pmid_convert_url, data)
    except Exception as e:
        logger.error('Error looking up PMID in PMC: %s' % e)
        return {}
    if tree is None:
        return {}
    record = tree.find('record')
    if record is None:
        return {}
    doi = record.attrib.get('doi')
    pmid = record.attrib.get('pmid')
    pmcid = record.attrib.get('pmcid')
    ids = {'doi': doi,
           'pmid': pmid,
           'pmcid': pmcid}

```
