# Description
Parse a grounding entry string and generate grounding dictionary.

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

def parse_grounding_entry(entry):
    """Return a dict representing single grounding curation entry string."""
    entry = entry.strip()
    # We now try to match the standard pattern for grounding curation
    match = re.match(r'^\[(.*)\] -> ([^ ]+)$', entry)
    # We log any instances of curations that don't match the pattern
    if not match:
        logger.warning('"%s" does not match the grounding curation '
                       'pattern.' % entry)
        return None
    txt, dbid_str = match.groups()
    # We now get a dict of curated mappings to return
    try:
        dbid_entries = [entry.split(':', maxsplit=1)
                        for entry in dbid_str.split('|')]
        dbids = {k: v for k, v in dbid_entries}
    except Exception as e:
        logger.warning('Could not interpret DB IDs: %s for %s' %
                       (dbid_str, txt))
        return None

```
