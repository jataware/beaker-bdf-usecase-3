# Description
Retrieve the text content for articles given a list of their PMIDs.

# Code
```
import time
import logging
from indra.literature import pubmed_client, pmc_client, elsevier_client

logger = logging.getLogger(__name__)

# the elsevier_client will log messages that it is safe to ignore
el = logging.getLogger('indra.literature.elsevier_client')

def get_text_content_for_pmids(pmids):
    """Get text content for articles given a list of their pmids

    Parameters
    ----------
    pmids : list of str

    Returns
    -------
    text_content : list of str
    """
    pmc_pmids = set(pmc_client.filter_pmids(pmids, source_type='fulltext'))

    pmc_ids = []
    for pmid in pmc_pmids:
        pmc_id = pmc_client.id_lookup(pmid, idtype='pmid')['pmcid']
        if pmc_id:
            pmc_ids.append(pmc_id)
        else:
            pmc_pmids.discard(pmid)

    pmc_xmls = []
    failed = set()
    for pmc_id in pmc_ids:
        if pmc_id is not None:
            pmc_xmls.append(pmc_client.get_xml(pmc_id))
        else:
            failed.add(pmid)
        time.sleep(0.5)

    remaining_pmids = set(pmids) - pmc_pmids | failed
    abstracts = []
    for pmid in remaining_pmids:
        abstract = pubmed_client.get_abstract(pmid)
        abstracts.append(abstract)
        time.sleep(0.5)

    return [text_content for source in (pmc_xmls, abstracts)

```
