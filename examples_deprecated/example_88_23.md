# Description
A test for grounding statements using Gilda.

# Code
```
from indra.preassembler.grounding_mapper.gilda import ground_statements

def test_ground_gilda():
    for mode in ['web', 'local']:
        mek = Agent('Mek', db_refs={'TEXT': 'MEK'})
        erk = Agent('Erk1', db_refs={'TEXT': 'Erk1'})
        stmt = Phosphorylation(mek, erk)
        grounded_stmts = ground_statements([stmt], mode=mode)
        stmt = grounded_stmts[0]
        assert stmt.enz.name == 'MEK', stmt.enz
        assert stmt.enz.db_refs['FPLX'] == 'MEK'
        assert stmt.sub.name == 'MAPK3'
        assert stmt.sub.db_refs['HGNC'] == '6877'

```
