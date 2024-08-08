# Description
Test the creation of a PyBEL model with simple phosphorylation and ubiquitination statements.

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
ub_dsl = pmod('Ub', 'Ser', 218)
braf_dsl = protein(namespace='HGNC', name='BRAF', identifier='1097')
map2k1_dsl = protein(namespace='HGNC', name='MAP2K1', identifier='6840')

def get_edge_data(g, u, v):
    assert g.has_edge(u, v)
    data = g.get_edge_data(u, v)

def test_simple_modification_no_evidence():
    braf = Agent('BRAF', db_refs={'HGNC': '1097', 'UP': 'P15056'})
    braf_kin = Agent('BRAF', activity=ActivityCondition('kinase', True),
                     db_refs={'HGNC': '1097', 'UP': 'P15056'})
    braf_cat = Agent('BRAF', activity=ActivityCondition('catalytic', True),
                     db_refs={'HGNC': '1097', 'UP': 'P15056'})
    map2k1 = Agent('MAP2K1', db_refs={'HGNC': '6840', 'UP': 'Q02750'})  # MEK
    stmt1 = Phosphorylation(braf, map2k1, 'S', '218')
    stmt2 = Phosphorylation(braf_kin, map2k1, 'S', '218')
    stmt3 = Ubiquitination(braf_cat, map2k1, 'S', '218')
    # Edge info for subject
    edge1 = None
    edge2 = activity('kin')
    edge3 = activity('cat')
    for stmt, modtuple, subj_edge in ((stmt1, phos_dsl, edge1),
                                      (stmt2, phos_dsl, edge2),
                                      (stmt3, ub_dsl, edge3)):
        pba = pa.PybelAssembler([stmt])
        belgraph = pba.make_model()
        assert belgraph.number_of_nodes() == 3, belgraph.number_of_nodes()
        map2k1_mod_dsl = map2k1_dsl.with_variants(modtuple)
        assert set(belgraph) == {braf_dsl, map2k1_dsl, map2k1_mod_dsl}, \
            (set(belgraph), {braf_dsl, map2k1_dsl, map2k1_mod_dsl})
        assert belgraph.number_of_edges() == 2, belgraph.number_of_edges()
        assert belgraph.has_edge(map2k1_dsl, map2k1_mod_dsl)
        assert belgraph.has_edge(braf_dsl, map2k1_mod_dsl)
        edge_data = get_edge_data(belgraph, braf_dsl, map2k1_mod_dsl)
        assert edge_data[pc.RELATION] == pc.INCREASES

```
