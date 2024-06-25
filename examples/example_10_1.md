# Description
Return the PubChem ID corresponding to a given ChEBI ID. It utilizes the `chebi_pubchem` dictionary to perform the lookup by calling the helper function `_add_prefix`.

# Code
```
import os
import logging
import requests
from lxml import etree
from functools import lru_cache, cmp_to_key
from indra.util import read_unicode_csv
from indra.databases.obo_client import OboClient

_obo_client = OboClient(prefix='chebi')

logger = logging.getLogger(__name__)

# Namespaces used in the XML
chebi_xml_ns = {'n': 'http://schemas.xmlsoap.org/soap/envelope/',
                'c': 'https://www.ebi.ac.uk/webservices/chebi'}

chebi_pubchem, pubchem_chebi = _read_chebi_to_pubchem()

def _add_prefix(chid):
    if chid and not chid.startswith('CHEBI:'):
        return 'CHEBI:%s' % chid
    else:

def get_pubchem_id(chebi_id):
    """Return the PubChem ID corresponding to a given ChEBI ID.

    Parameters
    ----------
    chebi_id : str
        ChEBI ID to be converted.

    Returns
    -------
    pubchem_id : str
        PubChem ID corresponding to the given ChEBI ID. If the lookup fails,
        None is returned.
    """
    pubchem_id = chebi_pubchem.get(_add_prefix(chebi_id))

```
