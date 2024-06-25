# Description
Illustrates handling DOI citations within graph evidence.

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

def test_doi_evidence():
    """Test processing edges with DOI citations."""
    mek = Protein(name='MAP2K1', namespace='HGNC')
    erk = Protein(name='MAPK1', namespace='HGNC')
    g = BELGraph()
    g.annotation_list['TextLocation'] = {'Abstract'}
    ev_doi = '123456'
    g.add_directly_increases(
        mek, erk, evidence='Some evidence.',
        citation=('doi', ev_doi),
        annotations={"TextLocation": 'Abstract'},
    )
    pbp = bel.process_pybel_graph(g)
    assert pbp.statements
    assert len(pbp.statements) == 1
    assert len(pbp.statements[0].evidence) == 1
    ev = pbp.statements[0].evidence[0]
    assert ev.pmid is None
    assert 'DOI' in ev.text_refs

```
