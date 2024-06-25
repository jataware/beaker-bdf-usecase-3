# Description
Tests the retrieval of text references from a PubMed Central (PMC) URL.

# Code
```
import pytest
from gilda import ground
from indra.sources import hypothesis, trips
from indra.statements import *
from indra.sources.hypothesis.processor import HypothesisProcessor, parse_context_entry, parse_grounding_entry, get_text_refs

def test_get_text_refs_pmcid():
    url = 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7071777/'
    refs = get_text_refs(url)
    assert refs.get('PMCID') == 'PMC7071777', refs

```
