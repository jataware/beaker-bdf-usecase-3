# Description
Parses invalid grounding entries and asserts that they are parsed as None.

# Code
```
import pytest
from gilda import ground
from indra.sources import hypothesis, trips
from indra.statements import *
from indra.sources.hypothesis.processor import HypothesisProcessor, parse_context_entry, parse_grounding_entry, get_text_refs

def test_parse_invalid_grounding_entry():
    entries = ['xxx', '[xxx]->a', 'xxx -> a', 'xxx -> a:1&b:4']
    for entry in entries:

```
