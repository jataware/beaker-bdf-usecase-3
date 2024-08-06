# Description
Gets the annotation text from INDRA statements with various configurations of grounded and ungrounded agents.

# Code
```
import pytest
from gilda import ground
from indra.sources import hypothesis, trips
from indra.statements import *
from indra.sources.hypothesis.processor import HypothesisProcessor, parse_context_entry, parse_grounding_entry, get_text_refs

def test_get_annotation_text():
    # Test statement with multiple grounded agents
    stmt = Inhibition(
        Agent('vemurafenib', db_refs={'CHEBI': 'CHEBI:63637'}),
        Agent('BRAF', db_refs={'HGNC': '1097'})
    )
    annot_text = get_annotation_text(stmt, annotate_agents=True)
    assert annot_text == \
        '[vemurafenib](https://identifiers.org/CHEBI:63637) inhibits ' \
        '[BRAF](https://identifiers.org/hgnc:1097).', annot_text
    annot_text = get_annotation_text(stmt, annotate_agents=False)
    assert annot_text == 'Vemurafenib inhibits BRAF.', annot_text

    # Test statement with ungrounded and None agents
    stmt = Phosphorylation(None, Agent('X'))
    annot_text = get_annotation_text(stmt, annotate_agents=True)
    assert annot_text == 'X is phosphorylated.', annot_text
    annot_text = get_annotation_text(stmt, annotate_agents=False)

```
