# Description
Tests the retrieval of text references from a bioRxiv URL.

# Code
```
import pytest
from gilda import ground
from indra.sources import hypothesis, trips
from indra.statements import *
from indra.sources.hypothesis.processor import HypothesisProcessor, parse_context_entry, parse_grounding_entry, get_text_refs

def test_get_text_refs_biorxiv():
    url = 'https://www.biorxiv.org/content/10.1101/2020.04.16.044016v1'
    refs = get_text_refs(url)
    assert refs.get('URL') == url, refs
    assert refs.get('DOI') == '10.1101/2020.04.16.044016', refs
    url = 'https://www.biorxiv.org/content/10.1101/2020.04.16.044016v1.full'
    refs = get_text_refs(url)
    assert refs.get('URL') == url, refs

```
