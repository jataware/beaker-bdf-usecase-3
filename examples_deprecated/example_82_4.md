# Description
This example shows how to expand families within `Activation` and `Phosphorylation` statements and verifies that expanded agents contain 'TEXT', 'UP', and 'HGNC' keys in their db_refs.

# Code
```
import itertools
from indra.ontology.bio import bio_ontology
from indra.tools.expand_families import Expander
from indra.statements import Agent, Activation, Phosphorylation

# Get the Expander

def test_db_ref_keys():
    # test that expanded families get TEXT, UP, HGNC keys in their db_refs
    # Declare some agents
    grb2 = Agent('GRB2',
                 db_refs={'TEXT': 'Grb2', 'UP': 'P62993', 'HGNC': '4566'})
    shc = Agent('SHC', db_refs={'FPLX': 'SHC'})
    # Test case where one agent is a family and the other is a gene
    st = Activation(grb2, shc)
    expanded_stmts = exp.expand_families([st])
    for st in expanded_stmts:
        for agent in st.agent_list():
            if agent is not None:
                assert set(agent.db_refs) >= {'TEXT', 'UP', 'HGNC'}, \
                    agent.db_refs
    # Test for case involving None for one of the agents
    st = Phosphorylation(None, shc)
    expanded_stmts = exp.expand_families([st])
    for st in expanded_stmts:
        for agent in st.agent_list():
            if agent is not None:
                assert set(agent.db_refs) >= {'TEXT', 'UP', 'HGNC'}
    # Statement with two families: 4x4 SHC
    st = Activation(shc, shc)
    expanded_stmts = exp.expand_families([st])
    for st in expanded_stmts:
        for agent in st.agent_list():
            if agent is not None:

```
