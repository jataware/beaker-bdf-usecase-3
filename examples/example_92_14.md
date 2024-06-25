# Description
Converts a statement with multiple evidence entries to annotations.

# Code
```
import pytest
from gilda import ground
from indra.sources import hypothesis, trips
from indra.statements import *
from indra.sources.hypothesis.processor import HypothesisProcessor, parse_context_entry, parse_grounding_entry, get_text_refs

def test_statement_to_annotations():
    evs = [
        # This will get filtered out
        Evidence(source_api='reach'),
        # This will get added as an annotation
        Evidence(source_api='sparser', text='some text 1',
                 pmid='12345'),
    ]
    stmt = Dephosphorylation(None, Agent('X'), evidence=evs)
    annots = statement_to_annotations(stmt)
    assert len(annots) == 1

```
