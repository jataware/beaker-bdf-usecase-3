# Description
Generate text references from a URL.

# Code
```
import re
import logging
from indra.statements import BioContext, RefContext
from indra.ontology.bio import bio_ontology
from indra.ontology.standardize import standardize_db_refs
from gilda import ground

logger = logging.getLogger(__name__)

allowed_contexts = {
    'Location': 'location',
    'Cell line': 'cell_line',
    'Cell type': 'cell_type',
    'Organ': 'organ',
    'Disease': 'disease',
    'Species': 'species'

def get_text_refs(url):
    """Return the parsed out text reference dict from an URL."""
    text_refs = {'URL': url}
    match = re.match(r'https://www.ncbi.nlm.nih.gov/pubmed/(\d+)', url)
    if match:
        text_refs['PMID'] = match.groups()[0]
    match = re.match(r'https://www.ncbi.nlm.nih.gov/pmc/articles/(PMC\d+)/',
                     url)
    if match:
        text_refs['PMCID'] = match.groups()[0]
    match = re.match(r'https://www.biorxiv.org/content/([^v]+)v', url)
    if match:
        text_refs['DOI'] = match.groups()[0]

```
