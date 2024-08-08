# Description
Extract groundings from annotations using HypothesisProcessor.

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

    def extract_groundings(self):
        """Sets groundings attribute to list of extracted groundings."""
        for annotation in self.annotations:
            tags = annotation.get('tags')
            if tags and 'gilda' in tags:
                groundings = self.groundings_from_annotation(annotation)
                if groundings:
                    for txt, refs in groundings.items():
                        if txt in self.groundings and \
                                (self.groundings[txt] != refs):
                            logger.info(
                                'There is already a curation for %s: %s, '
                                'overwriting with %s' % (txt,
                                                         str(groundings[txt]),
                                                         str(refs)))


```
