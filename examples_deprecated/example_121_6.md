# Description
Test the creation of a PyBEL model that includes inhibition statements.

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

braf_dsl = protein(namespace='HGNC', name='BRAF', identifier='1097')
map2k1_dsl = protein(namespace='HGNC', name='MAP2K1', identifier='6840')

def get_first_edge_data(g):

def test_inhibition():
    braf_kin = Agent('BRAF', activity=ActivityCondition('kinase', True),
                     db_refs={'HGNC': '1097', 'UP': 'P15056'})
    mek = Agent('MAP2K1', db_refs={'HGNC': '6840', 'UP': 'Q02750'})
    stmt = Inhibition(braf_kin, mek, 'kinase')
    stmt_hash = stmt.get_hash(refresh=True)
    edge = {
        pc.RELATION: pc.DECREASES,
        pc.SUBJECT: activity('kin'),
        pc.OBJECT: activity('kin'),
        pc.ANNOTATIONS: {
            'stmt_hash': {stmt_hash: True},
            'uuid': {stmt.uuid: True},
            'belief': {stmt.belief: True},
        },
    }
    pba = pa.PybelAssembler([stmt])
    belgraph = pba.make_model()
    assert belgraph.number_of_nodes() == 2, belgraph.number_of_nodes()
    assert braf_dsl in belgraph
    assert map2k1_dsl in belgraph
    assert belgraph.number_of_edges() == 1
    edge_data = get_first_edge_data(belgraph)

```
