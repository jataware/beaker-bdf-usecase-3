# Description
Tests the retrieval of text references from a PubMed URL.

# Code
```
import pytest
from gilda import ground
from indra.sources import hypothesis, trips
from indra.statements import *
from indra.sources.hypothesis.processor import HypothesisProcessor, parse_context_entry, parse_grounding_entry, get_text_refs

def test_get_text_refs_pmid():
    url = 'https://www.ncbi.nlm.nih.gov/pubmed/32196952'
    refs = get_text_refs(url)
    assert refs.get('PMID') == '32196952', refs

```
