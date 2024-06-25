# Description
Parses invalid context entries and asserts that they are parsed as None.

# Code
```
import pytest
from gilda import ground
from indra.sources import hypothesis, trips
from indra.statements import *
from indra.sources.hypothesis.processor import HypothesisProcessor, parse_context_entry, parse_grounding_entry, get_text_refs

def test_parse_invalid_context_entry():
    entries = ['xxx: yyy', 'Disease:something', 'xxx']
    for entry in entries:

```
