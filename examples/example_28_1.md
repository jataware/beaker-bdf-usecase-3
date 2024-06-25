# Description
Retrieve text content for articles that contain a particular gene using the gene's HGNC name.

# Code
```
import time
import logging
from indra.literature import pubmed_client, pmc_client, elsevier_client

logger = logging.getLogger(__name__)

# the elsevier_client will log messages that it is safe to ignore
el = logging.getLogger('indra.literature.elsevier_client')

def get_text_content_for_gene(hgnc_name):
    """Get articles that have been annotated to contain gene in entrez

    Parameters
    ----------
    hgnc_name : str
       HGNC name for gene

    Returns
    -------
    text_content : list of str
        xmls of fulltext if available otherwise abstracts for all articles
        that haven been annotated in entrez to contain the given gene
    """
    pmids = pubmed_client.get_ids_for_gene(hgnc_name)

```
