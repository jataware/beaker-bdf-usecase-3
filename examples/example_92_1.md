# Description
Processes INDRA annotations using the TRIPS reader and asserts the statements.

# Code
```
import pytest
from gilda import ground
from indra.sources import hypothesis, trips
from indra.statements import *
from indra.sources.hypothesis.processor import HypothesisProcessor, parse_context_entry, parse_grounding_entry, get_text_refs

@pytest.mark.nonpublic
@pytest.mark.slow
@pytest.mark.nogha
def test_process_indra_annnotations():
    hp = hypothesis.process_annotations(reader=trips.process_text)
    assert hp.statements
    for stmt in hp.statements:
        print(stmt)

```
