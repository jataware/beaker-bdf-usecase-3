# Description
This example demonstrates how to expand families within `Phosphorylation` statements using the Indra `Expander` class.

# Code
```
import itertools
from indra.ontology.bio import bio_ontology
from indra.tools.expand_families import Expander
from indra.statements import Agent, Phosphorylation

# Get the Expander

def test_expand_families():
    # Declare some agents
    akt = Agent('AKT', db_refs={'FPLX': 'AKT'})
    raf = Agent('RAF', db_refs={'FPLX': 'RAF'})
    mek = Agent('MEK', db_refs={'FPLX': 'MEK'})
    mapk1 = Agent('MAPK1', db_refs={'FPLX': 'MAPK1'})
    ampk = Agent('AMPK', db_refs={'FPLX': 'AMPK'})
    # Test case where one agent is a family and the other is a gene
    st = Phosphorylation(mek, mapk1)
    expanded_stmts = exp.expand_families([st])
    assert len(expanded_stmts) == 2
    # Test for case involving None for one of the agents
    st = Phosphorylation(None, akt)
    expanded_stmts = exp.expand_families([st])
    assert len(expanded_stmts) == 3
    # Statement with two families: 3 Rafs x 2 Meks
    st = Phosphorylation(raf, mek, 'S', '202')
    expanded_stmts = exp.expand_families([st])
    assert len(expanded_stmts) == 6
    # Test also for case involving both family and complex relationships
    st = Phosphorylation(ampk, mek)
    expanded_stmts = exp.expand_families([st])

```
