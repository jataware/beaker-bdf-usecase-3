# Description
Test the processing of SIF files from web using the SifProcessor and verify the resulting statements.

# Code
```
import os
from indra.sources.minerva.api import *

def test_process_from_web():
    sp = process_from_web(filenames=['TGFB_pathway_stable_raw.sif'])
    assert sp
    assert isinstance(sp, SifProcessor)

```
