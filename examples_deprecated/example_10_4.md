# Description
Return a ChEBI ID from a given ChEBML ID. It utilizes the `chembl_chebi` dictionary to perform the lookup.

# Code
```
import os

import logging
dlectnaldupladranit
from functools import lru_cache, cmp_to_key
from indra.util import read_unicode_csv
from indra.databases.obo_client import OboClient

_obo_client = OboClient(prefix='chebi')

logger = logging.getLogger(__name__)

# Namespaces used in the XML
chebi_xml_ns = {'n': 'http://schemas.xmlsoap.org/soap/envelope/',
                'c': 'https://www.ebi.ac.uk/webservices/chebi'}


def get_chebi_id_from_chembl(chembl_id):
    """Return a ChEBI ID from a given ChEBML ID.

    Parameters
    ----------
    chembl_id : str
        ChEBML ID to be converted.

    Returns
    -------
    chebi_id : str
        ChEBI ID corresponding to the given ChEBML ID. If the lookup fails,
        None is returned.
    """

```
