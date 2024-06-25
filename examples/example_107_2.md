# Description
Test the processing of a SIF file using the SifProcessor and verify the resulting statements.

# Code
```
import os
from indra.sources.minerva.api import *
from indra.sources.minerva.processor import SifProcessor
from indra.sources.minerva.minerva_client import get_model_ids

models_to_ids = get_model_ids()

def test_process_file():
    fname = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         'minerva_test1.sif')
    sp = process_file(fname, tgfb_id)
    assert sp
    assert isinstance(sp, SifProcessor)

```
