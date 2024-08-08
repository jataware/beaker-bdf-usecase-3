# Description
Example of querying a PyBEL neighborhood and validating the resulting statements.

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

title_ = hgnc_client.get_hgnc_id('MAP2K1')

def test_pybel_neighborhood_query():
    bp = bel.process_pybel_neighborhood(['TP63'],
                                        network_type='graph_jsongz_url',
                                        network_file=small_corpus_url)
    assert bp.statements
    for stmt in bp.statements:
        assert_valid_statement(stmt)
    assert all([s.evidence[0].context is not None
                for s in bp.statements])
    assert all([s.evidence[0].context.cell_line.name == 'MCF 10A'
               for s in bp.statements])
    # Locate statement about epidermis development
    stmt = [st for st in bp.statements if st.agent_list()[1].name ==
            'epidermis development'][0]
    assert repr(stmt.evidence[0].context) == str(stmt.evidence[0].context)
    assert stmt.evidence[0].context == BioContext(
        location=RefContext(name="Cytoplasm",
                            db_refs={'MESH': 'D003593'}),
        cell_line=RefContext(name="MCF 10A",
                             db_refs={'EFO': '0001200'}),
        cell_type=RefContext(name="keratinocyte",
                             db_refs={'CL': 'CL:0000312'}),
        organ=RefContext(name="colon",
                         db_refs={'UBERON': 'UBERON:0001155'}),
        disease=RefContext(name="cancer",
                           db_refs={'DOID': 'DOID:162'}),
        species=RefContext(name="Rattus norvegicus",
                           db_refs={'TAXONOMY': '10116'})), \
        stmt.evidence[0].context
    # Test annotation manager
    assert bp.annot_manager.get_mapping('Species', '9606') == \

```
