# Description
Get the citation count for a specific PMID by first converting it to a DOI using the CrossRef API, and then retrieving the citation count using the COCI API.

# Code
```
from typing import Union
import requests
from indra.literature.crossref_client import doi_query
coci_url = 'https://opencitations.net/index/coci/api/v1/'
citation_count_url = coci_url + 'citation-count/'
def get_citation_count_for_doi(doi: str) -> int:
    url = citation_count_url + doi
    res = requests.get(url)
    res.raise_for_status()

def get_citation_count_for_pmid(pmid: str) -> Union[int, None]:
    """Return the citation count for a given PMID.

    This uses the CrossRef API to get the DOI for the PMID, and then
    calls the COCI API to get the citation count for the DOI.

    If the DOI lookup failed, this returns None. Note that
    the COCI API returns a count of 0 for DOIs that are not
    indexed.

    Parameters
    ----------
    pmid :
        The PMID to get the citation count for.

    Returns
    -------
    :
        The citation count for the PMID.
    """
    doi = doi_query(pmid)
    if not doi:
        return None

```
