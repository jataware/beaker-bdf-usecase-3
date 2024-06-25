# Description
Parses a grounding entry and asserts the parsed dictionary structure.

# Code
```
import pytest
from gilda import ground
from indra.sources import hypothesis, trips
from indra.statements import *
from indra.sources.hypothesis.processor import HypothesisProcessor, parse_context_entry, parse_grounding_entry, get_text_refs

def test_parse_grounding_entry():
    entry = '[a and b] -> CHEBI:CHEBI:1234|PUBCHEM:5678'
    grounding = parse_grounding_entry(entry)
    assert grounding == {'a and b': {'CHEBI': 'CHEBI:1234',

```
