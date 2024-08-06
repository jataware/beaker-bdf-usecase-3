# Description
Test the creation of a PyBEL model with a phosphorylation statement that includes evidences.

# Code
```
import json
import networkx as nx
import pybel.constants as pc
from pybel.dsl import abundance, activity, bioprocess, complex_abundance, hgvs, pmod, protein, reaction
from indra.assemblers.pybel import assembler as pa
from indra.databases import hgnc_client
from indra.statements import *

def id(gene_name):
    return hgnc_client.get_hgnc_id(gene_name)

phos_dsl = pmod('Ph', 'Ser', 218)
braf_dsl = protein(namespace='HGNC', name='BRAF', identifier='1097')
map2k1_dsl = protein(namespace='HGNC', name='MAP2K1', identifier='6840')

def get_edge_data(g, u, v):
    assert g.has_edge(u, v)
    data = g.get_edge_data(u, v)

def test_modification_with_evidences():
    braf_kin = Agent('BRAF', activity=ActivityCondition('kinase', True),
                     db_refs={'HGNC': '1097', 'UP': 'P15056'})
    mek = Agent('MAP2K1', db_refs={'HGNC': '6840', 'UP': 'Q02750'})
    evidence = Evidence(source_api='test', text='evidence text', pmid='1234', epistemics={
        'dummy': ['a', 'b'],
        'scalar': 'yes',
        'missing': None,
    })
    stmt = Phosphorylation(braf_kin, mek, 'S', '218', evidence=evidence)
    pba = pa.PybelAssembler([stmt])
    belgraph = pba.make_model()
    assert belgraph.number_of_nodes() == 3, belgraph.number_of_nodes()
    assert braf_dsl in belgraph
    map2k1_mod_dsl = map2k1_dsl.with_variants(phos_dsl)
    assert map2k1_mod_dsl in belgraph
    assert belgraph.number_of_edges() == 2
    edge_data = get_edge_data(belgraph, braf_dsl, map2k1_mod_dsl)
    assert edge_data.get(pc.SUBJECT) == activity('kin')
    assert edge_data[pc.RELATION] == pc.INCREASES
    assert edge_data.get(pc.EVIDENCE) == 'evidence text', edge_data
    assert edge_data[pc.CITATION] == {
        pc.CITATION_DB: pc.CITATION_TYPE_PUBMED,
        pc.CITATION_IDENTIFIER: '1234',
    }
    assert 'source_api' in edge_data[pc.ANNOTATIONS]
    assert 'test' in edge_data[pc.ANNOTATIONS]['source_api']
    assert 'source_id' not in edge_data[pc.ANNOTATIONS]
    assert 'source_hash' in edge_data[pc.ANNOTATIONS]
    assert 'dummy' in edge_data[pc.ANNOTATIONS]
    assert 'a' in edge_data[pc.ANNOTATIONS]['dummy']
    assert 'b' in edge_data[pc.ANNOTATIONS]['dummy']
    assert 'scalar' in edge_data[pc.ANNOTATIONS]
    assert 'yes' in edge_data[pc.ANNOTATIONS]['scalar']

```
