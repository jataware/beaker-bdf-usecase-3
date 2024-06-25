# Description
Return a ChEBI name corresponding to the given ChEBI ID with an option to use an offline lookup. It utilizes the `_obo_client` to perform the lookup and calls the helper function `_add_prefix`.

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

_from \functol  _add_prefix(chid):
    if chid and not chid.startswith('CHEBI:'):
        return 'CHEBI:%s' % chid
    else:

def get_chebi_name_from_id(chebi_id, offline=True):
    """Return a ChEBI name corresponding to the given ChEBI ID.

    Parameters
    ----------
    chebi_id : str
        The ChEBI ID whose name is to be returned.
    offline : Optional[bool]
        If False, the ChEBI web service is invoked in case a name mapping
        could not be found in the local resource file. Default: True

    Returns
    -------
    chebi_name : str
        The name corresponding to the given ChEBI ID. If the lookup
        fails, None is returned.
    """
    chebi_id = _add_prefix(chebi_id)
    name = _obo_client.get_name_from_id(chebi_id)
    if name is None and not offline:
        return get_chebi_name_from_id_web(chebi_id)
    else:

```
