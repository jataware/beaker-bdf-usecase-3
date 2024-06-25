# Description
Extract INDRA Statements from annotations using HypothesisProcessor.

# Code
```
import re
import logging
from indra.statements import BioContext, RefContext
from indra.ontology.bio import bio_ontology
from indra.ontology.standardize import standardize_db_refs
from indra.sources import reach, bel
from gilda import ground

logger = logging.getLogger(__name__)

allowed_contexts = {
    'Location': 'location',
    'Cell line': 'cell_line',
    'Cell type': 'cell_type',
    'Organ': 'organ',
    'Disease': 'disease',
    'Species': 'species'

def extract_statements(self):
    """Sets statements attribute to list of extracted INDRA Statements."""
    for annotation in self.annotations:
        tags = annotation.get('tags')
        # Allow no tags or indra as a tag
        if not tags or 'indra' in tags:
            stmts = self.stmts_from_annotation(annotation)
            if stmts:

```
