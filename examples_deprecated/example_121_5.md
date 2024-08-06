# Description
Test the creation of a PyBEL model that includes direct activation statements with evidence.

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

def test_direct_activation():
    braf_no_act = Agent('BRAF', db_refs={'HGNC': '1097', 'UP': 'P15056'})
    braf_kin = Agent('BRAF', activity=ActivityCondition('kinase', True),
                     db_refs={'HGNC': '1097', 'UP': 'P15056'})
    mek = Agent('MAP2K1', db_refs={'HGNC': '6840', 'UP': 'Q02750'})
    stmt1_ev = Evidence(
        pmid='1234',
        epistemics={'direct': True},
    )
    stmt1 = Activation(braf_no_act, mek, evidence=stmt1_ev)
    stmt2 = Activation(braf_kin, mek, 'kinase', evidence=stmt1_ev)
    hash1 = stmt1.get_hash(refresh=True)
    hash2 = stmt2.get_hash(refresh=True)
    edge1 = {
        pc.RELATION: pc.DIRECTLY_INCREASES,
        pc.OBJECT: activity(),
        pc.EVIDENCE: 'No evidence text.',
        pc.CITATION: {
            pc.CITATION_DB: pc.CITATION_TYPE_PUBMED,
            pc.CITATION_IDENTIFIER: '1234',
        },
        pc.ANNOTATIONS: {
            'stmt_hash': {hash1: True},
            'source_hash': {stmt1_ev.get_source_hash(): True},
            'uuid': {stmt1.uuid: True},
            'belief': {stmt1.belief: True},
        },
    }
    edge2 = {
        pc.RELATION: pc.DIRECTLY_INCREASES,
        pc.SUBJECT: activity('kin'),
        pc.OBJECT: activity('kin'),
        pc.EVIDENCE: 'No evidence text.',
        pc.CITATION: {
            pc.CITATION_DB: pc.CITATION_TYPE_PUBMED,
            pc.CITATION_IDENTIFIER: '1234',
        },
        pc.ANNOTATIONS: {
            'stmt_hash': {hash2: True},
            'source_hash': {stmt1_ev.get_source_hash(): True},
            'uuid': {stmt2.uuid: True},
            'belief': {stmt2.belief: True},
        },
    }
    for stmt, expected_edge in ((stmt1, edge1), (stmt2, edge2)):
        pba = pa.PybelAssembler([stmt])
        belgraph = pba.make_model()
        assert belgraph.number_of_nodes() == 2, belgraph.number_of_nodes()
        assert braf_dsl in belgraph
        assert map2k1_dsl in belgraph
        assert belgraph.number_of_edges() == 1
        edge_data = get_first_edge_data(belgraph)

```
