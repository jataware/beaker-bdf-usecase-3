# Description
Return the ChEBI ID corresponding to a given PubChem ID. It utilizes the `pubchem_chebi` dictionary to perform the lookup.

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


def get_chebi_id_from_pubchem(pubchem_id):
    """Return the ChEBI ID corresponding to a given Pubchem ID.

    Parameters
    ----------
    pubchem_id : str
        Pubchem ID to be converted.

    Returns
    -------
    chebi_id : str
        ChEBI ID corresponding to the given Pubchem ID. If the lookup fails,
        None is returned.
    """

```
