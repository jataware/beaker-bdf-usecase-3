# Description
Generate groundings from a single annotation.

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

@staticmethod
def groundings_from_annotation(annotation):
    """Return a dict of groundings from a single annotation."""
    text = annotation.get('text')
    if not text:
        return {}
    parts = [t for t in text.split('\n') if t]
    groundings = {}
    for entry in parts:
        grounding = parse_grounding_entry(entry)
        if grounding:
            groundings.update(grounding)

```
