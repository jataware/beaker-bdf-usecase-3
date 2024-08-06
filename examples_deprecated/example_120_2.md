# Description
Example of processing a BEL JSON neighborhood.

# Code
```
import os
from urllib import request
from pybel import BELGraph
from pybel.dsl import *
from pybel.language import Entity
from pybel.io import from_nodelink_file
from pybel.examples import egf_graph
from indra.statements import *
from indra.sources import bel
from indra.sources.bel import processor as pb
from indra.sources.bel.api import process_cbn_jgif_file, process_pybel_graph, small_corpus_url
from indra.databases import hgnc_client

def test_process_jgif():
    test_file_url = 'https://s3.amazonaws.com/bigmech/travis/Hox-2.0-Hs.jgf'
    test_file = 'Hox-2.0-Hs.jgf'
    if not os.path.exists(test_file):
        request.urlretrieve(url=test_file_url, filename=test_file)
    pbp = process_cbn_jgif_file(test_file)

    # Clean up
    os.remove(test_file)

    assert len(pbp.statements) == 26, len(pbp.statements)
    assert isinstance(pbp.statements[0], Statement)

```
