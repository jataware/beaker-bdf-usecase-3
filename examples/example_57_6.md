# Description
Testing the belief engine's hierarchical probabilities with evidence hierarchies.

# Code
```
from copy import deepcopy
import pytest
from indra.statements import Evidence, Agent, Phosphorylation
from indra.belief import BeliefEngine, load_default_probs

default_probs = load_default_probs()
ev1 = Evidence(source_api='reach')

def test_hierarchy_probs1():
    be = BeliefEngine()
    st1 = Phosphorylation(None, Agent('a'), evidence=[ev1])
    st2 = Phosphorylation(None, Agent('b'), evidence=[ev2])
    st2.supports = [st1]
    st1.supported_by = [st2]
    be.set_hierarchy_probs([st1, st2])
    assert_close_enough(st1.belief, 1-0.35)

```
