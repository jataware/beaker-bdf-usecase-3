# Description
Parse context entry and generate context dictionary.

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

def parse_context_entry(entry, grounder, sentence=None):
    """Return a dict of context type and object processed from an entry."""
    match = re.match(r'(.*): (.*)', entry)
    if not match:
        return None
    context_type, context_txt = match.groups()
    if context_type not in allowed_contexts:
        logger.warning('Unknown context type %s' % context_type)
        return None

    terms = grounder(context_txt, context=sentence)
    if not terms:
        logger.warning('Could not ground %s context: %s'
                       % (context_type, context_txt))
    db_refs = {}
    if terms:
        db_refs = standardize_db_refs({terms[0].term.db:
                                       terms[0].term.id})
    db_refs['TEXT'] = context_txt
    standard_name = None
    if terms:
        standard_name = bio_ontology.get_name(terms[0].term.db,
                                              terms[0].term.id)
    name = standard_name if standard_name else context_txt
    context = RefContext(name=name, db_refs=db_refs)

```
