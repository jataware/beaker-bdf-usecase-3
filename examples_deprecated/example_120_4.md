# Description
Example of converting a BEL graph to statements and ensuring evidence is captured correctly.

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
from indra.statements.validate import assert_valid_statement

mek_hgnc_id = hgnc_client.get_hgnc_id('MAP2K1')

def test_phosphorylation_one_site_with_evidence():
    mek = Protein(name='MAP2K1', namespace='HGNC')
    erk = Protein(name='MAPK1', namespace='HGNC',
                  variants=[pmod('Ph', position=185, code='Thr')])
    g = BELGraph()
    g.annotation_list['TextLocation'] = {'Abstract'}
    ev_text = 'Some evidence.'
    ev_pmid = '123456'
    edge_hash = g.add_directly_increases(
        mek, erk, evidence=ev_text,
        citation=ev_pmid,
        annotations={"TextLocation": 'Abstract'},
    )
    pbp = bel.process_pybel_graph(g)
    assert pbp.statements
    assert len(pbp.statements) == 1
    assert isinstance(pbp.statements[0], Phosphorylation)
    assert pbp.statements[0].residue == 'T'
    assert pbp.statements[0].position == '185'
    enz = pbp.statements[0].enz
    sub = pbp.statements[0].sub
    assert enz.name == 'MAP2K1'
    assert enz.mods == []
    assert sub.name == 'MAPK1'
    assert sub.mods == []
    # Check evidence
    assert len(pbp.statements[0].evidence) == 1
    ev = pbp.statements[0].evidence[0]
    assert ev.source_api == 'bel'
    assert ev.source_id == edge_hash
    assert ev.pmid == ev_pmid, (ev.pmid, ev_pmid)
    assert ev.text == ev_text
    assert ev.annotations == {
        'bel': 'p(HGNC:MAP2K1) directlyIncreases '
               'p(HGNC:MAPK1, pmod(go:0006468 ! "protein phosphorylation", Thr, 185))'
    }

```
