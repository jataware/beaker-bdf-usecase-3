# Description
This example demonstrates how to use the `exp.expanded_complexes_from_hierarchy` method to get expanded complexes and ensure the expected hierarchical structures in the Indra framework.

# Code
```
import itertools
from indra.ontology.bio import bio_ontology
from indra.tools.expand_families import Expander
from indra.statements import Agent

# Get the Expander

def test_expanded_complexes_from_hierarchy():
    complexes = exp.expanded_complexes_from_hierarchy()
    stmt_ag_names = []
    for stmt in complexes:
        sorted_names = tuple(sorted([ag.name for ag in stmt.agent_list()]))
        stmt_ag_names.append(sorted_names)
    ampk_alphas = ('PRKAA1', 'PRKAA2')
    ampk_betas = ('PRKAB1', 'PRKAB2')
    ampk_gammas = ('PRKAG1', 'PRKAG2', 'PRKAG3')
    for alpha, beta, gamma in itertools.product(ampk_alphas, ampk_betas,
                                                ampk_gammas):
        assert tuple(sorted((alpha, beta, gamma))) in stmt_ag_names, \

```
