# Description
This example shows how to use the `exp.complexes_from_hierarchy` method to retrieve complexes and check their validity by matching keys in the Indra framework.

# Code
```
import itertools
from indra.ontology.bio import bio_ontology
from indra.tools.expand_families import Expander
from indra.statements import Agent, Complex

# Get the Expander

def test_complexes_from_hierarchy():
    complexes = exp.complexes_from_hierarchy()
    keys = [c.matches_key() for c in complexes]
    probe_stmt = Complex([Agent('AMPK_alpha', db_refs={'FPLX': 'AMPK_alpha'}),
                          Agent('AMPK_beta', db_refs={'FPLX': 'AMPK_beta'}),
                          Agent('AMPK_gamma', db_refs={'FPLX': 'AMPK_gamma'})])

```
