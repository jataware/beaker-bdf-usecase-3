# Description
Test assembling an IncreaseAmount statement into an Index Card and validating it against a JSON schema.

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

def test_assemble_regulateamount():
    stmt = IncreaseAmount(braf, map2k1, evidence=ev)
    card = IndexCardAssembler.assemble_one_card(stmt)
    card.card['pmc_id'] = get_pmc_id(stmt)
    print(card.get_string())
    print()

```
