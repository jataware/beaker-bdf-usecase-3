# Description
Test the processing of multiple SIF files using the SifProcessor and verify the resulting statements.

# Code
```
import os
from indra.sources.minerva.api import *
from indra.sources.minerva.processor import SifProcessor
from indra.sources.minerva.minerva_client import get_model_ids

models_to_ids = get_model_ids()
tgfb_id = models_to_ids['TGFbeta signalling']

def test_process_files():
    fname1 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          'minerva_test1.sif')
    fname2 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          'minerva_test2.sif')
    # One file
    sp = process_files({tgfb_id: fname1})
    assert sp
    assert isinstance(sp, SifProcessor)
    assert len(sp.statements) == 2
    # Multiple files
    sp = process_files({tgfb_id: fname1, apopt_id: fname2})
    assert sp
    assert isinstance(sp, SifProcessor)

```
