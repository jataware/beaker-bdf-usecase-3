# Description
Parses a context entry and asserts the parsed dictionary structure and content.

# Code
```
import pytest
from gilda import ground
from indra.sources import hypothesis, trips
from indra.statements import *
from indra.sources.hypothesis.processor import HypothesisProcessor, parse_context_entry, parse_grounding_entry, get_text_refs

def test_parse_context_entry():
    context_dict = parse_context_entry('Cell type: antigen presenting cells',
                                       ground, 'antigen presenting cells')
    assert len(context_dict) == 1
    assert 'cell_type' in context_dict
    ref_context = context_dict['cell_type']
    assert ref_context.name == 'Antigen-Presenting Cells', ref_context
    assert ref_context.db_refs.get('MESH') == 'D000938'

```
