# Description
Retrieve PMIDs from the processed CX file and validate them

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
import os
from indra.sources.ndex_cx import process_cx_file
from indra.sources.ndex_cx.processor import NdexCxProcessor
path_this = os.path.dirname(os.path.abspath(__file__))

def test_get_pmids():
    pmids = ncp_file.get_pmids()
    for pmid in pmids:
        # Make sure all of the entries are valid integers
        assert isinstance(pmid, str)

```
