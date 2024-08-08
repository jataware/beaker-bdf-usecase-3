# Description
Test the creation of a PyBEL model that includes increase amount statements with transcription activity.

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

mdm2_dsl = protein(namespace='HGNC', name='MDM2', identifier='6973')
tp53_dsl = protein(namespace='HGNC', name='TP53', identifier='11998')
def get_first_edge_data(g):

def test_increase_amount_tscript():
    tp53 = Agent('TP53', activity=ActivityCondition('transcription', True),
                 db_refs={'HGNC': '11998'})
    mdm2 = Agent('MDM2', db_refs={'HGNC': '6973'})

    stmt = IncreaseAmount(tp53, mdm2)
    pba = pa.PybelAssembler([stmt])
    belgraph = pba.make_model()
    assert belgraph.number_of_nodes() == 2, belgraph.number_of_nodes()
    assert mdm2_dsl in belgraph
    assert tp53_dsl in belgraph
    assert belgraph.number_of_edges() == 1
    edge_data = get_first_edge_data(belgraph)
    assert edge_data[pc.RELATION] == pc.INCREASES

```
