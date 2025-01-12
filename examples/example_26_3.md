# Description
Retrieve the preferred compound IDs for a given PubChem CID.

# Code
```
import logging
import requests
from functools import lru_cache

pubchem_url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug'
logger = logging.getLogger(__name__)

@lru_cache(maxsize=5000)
def get_json_record(pubchem_cid):
    url = (pubchem_url + '_view/data/compound/%s/JSON/') % pubchem_cid
    res = requests.get(url)

def get_preferred_compound_ids(pubchem_cid):
    """Return a list of preferred CIDs for a given PubChem CID.

    Parameters
    ----------
    pubchem_cid : str
        The PubChem CID whose preferred CIDs should be returned.

    Returns
    -------
    list of str
        The list of preferred CIDs for the given CID. If there are no
        preferred CIDs for the given CID then an empty list is returned.
    """
    record = get_json_record(pubchem_cid)
    sections = record['Record']['Section']
    pref_ids = set()
    for section in sections:
        if section['TOCHeading'] == 'Preferred Compound':
            for pref_cpd in section['Information']:
                pref_ids |= set(pref_cpd['Value']['Number'])
    pref_ids = sorted([str(pid) for pid in pref_ids])

```
