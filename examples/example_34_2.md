# Description
Example code demonstrating how to retrieve XML for an article from a PMC ID.

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

def get_xml(pmc_id):
    """Returns XML for the article corresponding to a PMC ID."""
    if pmc_id.upper().startswith('PMC'):
        pmc_id = pmc_id[3:]
    # Request params
    params = {}
    params['verb'] = 'GetRecord'
    params['identifier'] = 'oai:pubmedcentral.nih.gov:%s' % pmc_id
    params['metadataPrefix'] = 'pmc'
    # Submit the request
    res = requests.get(pmc_url, params)
    if not res.status_code == 200:
        logger.warning("Couldn't download %s" % pmc_id)
        return None
    # Read the bytestream
    xml_bytes = res.content
    # Check for any XML errors; xml_str should still be bytes
    tree = ET.XML(xml_bytes, parser=UTB())
    xmlns = "http://www.openarchives.org/OAI/2.0/"
    err_tag = tree.find('{%s}error' % xmlns)
    if err_tag is not None:
        err_code = err_tag.attrib['code']
        err_text = err_tag.text
        logger.warning('PMC client returned with error %s: %s'
                       % (err_code, err_text))
        return None
    # If no error, return the XML as a unicode string
    else:

```
