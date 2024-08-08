# Description
Test the creation of a PyBEL model with a Gap statement.

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
def get_edge_data(g, u, v):
    assert g.has_edge(u, v)
    data = g.get_edge_data(u, v)
    return list(data.values())[0]


def test_gap():
    gap = Agent('RASA1', mods=[ModCondition('phosphorylation')],
                db_refs={'HGNC': '9871'})
    ras = Agent('KRAS', db_refs={'HGNC': '6407'})
    stmt = Gap(gap, ras)
    stmt_hash = stmt.get_hash(refresh=True)
    pba = pa.PybelAssembler([stmt])
    belgraph = pba.make_model()
    assert len(belgraph) == 3
    assert belgraph.number_of_edges() == 2

    gap_reference_node = protein(
        namespace='HGNC', name='RASA1', identifier='9871')
    gap_node = gap_reference_node.with_variants(pmod('Ph'))
    ras_node = protein(namespace='HGNC', name='KRAS', identifier='6407')

    assert gap_reference_node in belgraph
    assert gap_node in belgraph
    assert ras_node in belgraph
    edge_data = get_edge_data(belgraph, gap_node, ras_node)
    edge = {
        pc.RELATION: pc.DIRECTLY_DECREASES,
        pc.SUBJECT: activity('gap'),
        pc.OBJECT: activity('gtp'),
        pc.ANNOTATIONS: {
            'stmt_hash': {stmt_hash: True},
            'uuid': {stmt.uuid: True},
            'belief': {stmt.belief: True},
        },
    }

```
