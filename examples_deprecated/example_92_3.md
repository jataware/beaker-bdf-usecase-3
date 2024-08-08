# Description
Tests the extraction of statement annotations using the TRIPS reader and a sample annotation.

# Code
```
import pytest
from gilda import ground
from indra.sources import hypothesis, trips
from indra.statements import *
from indra.sources.hypothesis.processor import HypothesisProcessor, parse_context_entry, parse_grounding_entry, get_text_refs
from indra.sources.hypothesis.annotator import statement_to_annotations, evidence_to_annotation, get_annotation_text
grounding_annot_example = {
 'uri': 'https://en.wikipedia.org/wiki/Hydroxychloroquine',
 'text': '[Plaquenil] -> CHEBI:CHEBI:5801\n\n[HCQ] -> CHEBI:CHEBI:5801',
 'tags': ['gilda'],
 'target': [{'source': 'https://en.wikipedia.org/wiki/Hydroxychloroquine'}],
 'document': {'title': ['Hydroxychloroquine - Wikipedia']},
}

statement_annot_example = {
 'id': '4nBYAmqwEeq1ujf13__Y-w',
 'uri': 'https://www.ncbi.nlm.nih.gov/pubmed/32190173',
 'text': 'AMPK activates STAT3\nOrgan: liver\nLocation: nucleus',
 'tags': [],

@pytest.mark.slow
def test_statement_annotation():
    hp = HypothesisProcessor(annotations=[statement_annot_example],
                             reader=trips.process_text)
    hp.extract_statements()
    assert len(hp.statements) == 1
    stmt = hp.statements[0]
    assert stmt.subj.name == 'AMPK'
    assert stmt.obj.name == 'STAT3'
    context = stmt.evidence[0].context
    assert context.location.name == 'nucleus', context
    assert context.location.db_refs == {'GO': 'GO:0005634', 'TEXT': 'nucleus'}
    assert context.organ.name == 'Liver', context

```
