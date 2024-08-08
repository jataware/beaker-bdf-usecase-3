# Description
Parses an ungrounded context entry and asserts the parsed dictionary structure and content.

# Code
```
import pytest
from gilda import ground
from indra.sources import hypothesis, trips
from indra.statements import *
from indra.sources.hypothesis.processor import HypothesisProcessor, parse_context_entry, parse_grounding_entry, get_text_refs

def test_parse_ungrounded_context_entry():
    entry = 'Cell type: CD4+ T-cells'
    context_dict = parse_context_entry(entry, ground)
    assert len(context_dict['cell_type'].db_refs) == 1, \
        context_dict['cell_type'].db_refs
    assert context_dict['cell_type'].db_refs['TEXT'] == \

```
