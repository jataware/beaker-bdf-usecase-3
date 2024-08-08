# Description
Test the creation of a PyBEL model with a phosphorylation statement that includes mutation.

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

def test_modification_with_mutation():
    braf = Agent('BRAF', mutations=[MutCondition('600', 'V', 'E')],
                 db_refs={'HGNC': '1097', 'UP': 'P15056'})
    mek = Agent('MAP2K1', db_refs={'HGNC': '6840', 'UP': 'Q02750'})
    stmt = Phosphorylation(braf, mek, 'S', '218')
    pba = pa.PybelAssembler([stmt])
    belgraph = pba.make_model()
    # Adds in the base protein nodes as well as the variants (so 4 nodes)
    assert belgraph.number_of_nodes() == 4, belgraph.number_of_nodes()
    braf_mut_dsl = braf_dsl.with_variants(hgvs('p.Val600Glu'))

```
