# Description
Converts evidence to annotation and tests with various text references.

# Code
```
import pytest
from gilda import ground
from indra.sources import hypothesis, trips
from indra.statements import *
from indra.sources.hypothesis.processor import HypothesisProcessor, parse_context_entry, parse_grounding_entry, get_text_refs

def test_evidence_to_annot():
    # No evidence text
    ev = Evidence(source_api='reach')
    assert evidence_to_annotation(ev) is None

    # No text refs
    ev = Evidence(source_api='reach', text='Some text')
    assert evidence_to_annotation(ev) is None

    # Various text refs
    ev = Evidence(source_api='reach', text='Some text',
                  pmid='12345')
    annot = evidence_to_annotation(ev)
    assert annot == {'url': 'https://pubmed.ncbi.nlm.nih.gov/12345/',
                     'target_text': 'Some text',
                     'tags': ['reach']}, annot

    ev = Evidence(source_api='reach', text='Some text',
                  pmid=None, text_refs={'PMCID': '12345'})
    annot = evidence_to_annotation(ev)
    assert annot['url'] == 'https://www.ncbi.nlm.nih.gov/pmc/articles/12345/'


    ev = Evidence(source_api='reach', text='Some text',
                  pmid=None, text_refs={'URL': 'https://wikipedia.org'})
    annot = evidence_to_annotation(ev)

```
