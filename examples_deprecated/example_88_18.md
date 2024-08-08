# Description
A test for grounding agents with both HGNC ID and symbol.

# Code
```
from indra.preassembler.grounding_mapper import GroundingMapper

def test_map_entry_hgnc_and_up():
    """Make sure that HGNC symbol is replaced with HGNC ID when grounding map
    includes both UP ID and HGNC symbol."""
    rela = Agent('NF-kappaB p65', db_refs={'TEXT': 'NF-kappaB p65'})
    erk = Agent('ERK1', db_refs={'TEXT': 'ERK1'})
    stmt = Phosphorylation(erk, rela)
    g_map = {'NF-kappaB p65': {'TEXT': 'NF-kappaB p65', 'UP': 'Q04206',
                               'HGNC': '9955'}}
    gm = GroundingMapper(g_map)
    mapped_stmts = gm.map_stmts([stmt])
    assert len(mapped_stmts) == 1
    ms = mapped_stmts[0]
    assert ms.sub.db_refs == \
           {'TEXT': 'NF-kappaB p65', 'UP': 'Q04206',

```
