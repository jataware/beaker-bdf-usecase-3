# Description
Test assembling a phosphorylation statement into an Index Card and validating it against a JSON schema.

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

def test_assemble_phosphorylation():
    card = IndexCardAssembler.assemble_one_card(stmt_phos)
    card.card['pmc_id'] = get_pmc_id(stmt_phos)
    print(card.get_string())
    print()

```
