# Description
Test the `process_text_bio` function from the `indra.sources.eidos` library with a mock Eidos JSON response to confirm that it generates an `Activation` statement.

# Code
```
import os
import json
from unittest.mock import patch
from indra.sources import eidos
from indra.statements import Activation

path_this = os.path.dirname(os.path.abspath(__file__))

def _read_eidos_sentence_json():
    jsonld = os.path.join(path_this, 'eidos_bio_abstract.json')
    with open(jsonld, 'r') as fh:
        js = json.load(fh)

@patch('indra.sources.eidos.api._run_eidos_on_text')
def test_process_text_bio(mock_read):
    mock_read.return_value = _read_eidos_sentence_json()
    ep = eidos.process_text_bio('virus increases death')
    assert ep is not None
    assert len(ep.statements) == 1
    stmt = ep.statements[0]
    from indra.statements import Activation

```
