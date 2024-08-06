# Description
Test assembling multiple statements into an Index Card, making a model, printing it, and saving it.

# Code
```
import jsonschema
from os.path import dirname, abspath, join
from indra.assemblers.index_card.assembler import *
schema_path = join(dirname(abspath(__file__)), '../resources/index_card_schema.json')
with open(schema_path, 'rt') as fh:
    schema = json.load(fh)

braf = Agent('BRAF', db_refs={'UP': 'P15056'})
map2k1 = Agent('MAP2K1', db_refs={'HGNC': '6840'})
ev = Evidence(source_api='reach', text='BRAF phosphorylates MAP2K1.', pmid='22833081')
brafmut = Agent('BRAF', db_refs={'UP': 'P15056'}, mods=[ModCondition('phosphorylation', 'S', '596')], mutations=[MutCondition('600', 'V', 'E')], bound_conditions=[BoundCondition(Agent('BRAF'), True)])
stmt_phos = Phosphorylation(braf, map2k1, 'S', '222', evidence=ev)

def test_assemble_multiple():
    ia = IndexCardAssembler(pmc_override='PMC1234567')
    ia.add_statements([stmt_phos, stmt_dephos])
    ia.make_model()
    ia.print_model()

```
