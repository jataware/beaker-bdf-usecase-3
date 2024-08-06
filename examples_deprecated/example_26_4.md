# Description
Retrieve depositor provided PMIDs for a given PubChem CID.

# Code
```
import logging
import requests
from typing import List

pubchem_url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug'

def get_pmids(pubchem_cid: str) -> List[str]:
    """Return depositor provided PMIDs for a given PubChem CID.

    Note that this information can also be obtained via PubMed
    at https://www.ncbi.nlm.nih.gov/sites/entrez?LinkName=pccompound_pubmed&db=pccompound&cmd=Link&from_uid=<pubchem_cid>.

    Parameters
    ----------
    pubchem_cid :
        The PubChem CID whose PMIDs will be returned.

    Returns
    -------
    :
        PMIDs corresponding to the given PubChem CID. If none present,
        or the query fails, an empty list is returned.
    """
    url = '%s/compound/cid/%s/xrefs/PubMedID/JSON' % \
          (pubchem_url, pubchem_cid)
    res = requests.get(url)
    if res.status_code != 200:
        logger.error('Could not retrieve PMIDs for %s' % pubchem_cid)
        return []
    res_json = res.json()
    pmids_list = [str(pmid) for pmid in
                  res_json['InformationList']['Information'][0]['PubMedID']]

```
