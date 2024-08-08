# Description
Testing the belief engine's hierarchical probabilities with a more complex hierarchy of evidence.

# Code
```
from copy import deepcopy
import pytest
from indra.statements import Evidence, Agent, Phosphorylation
from indra.belief import BeliefEngine, load_default_probs

default_probs = load_default_probs()
ev1 = Evidence(source_api='reach')
ev2 = Evidence(source_api='trips')

def test_hierarchy_probs2():
    be = BeliefEngine()
    st1 = Phosphorylation(None, Agent('a'), evidence=[ev1])
    st2 = Phosphorylation(None, Agent('b'), evidence=[ev2])
    st3 = Phosphorylation(None, Agent('c'), evidence=[ev4])
    st2.supports = [st1]
    st3.supports = [st1, st2]
    st1.supported_by = [st2, st3]
    st2.supported_by = [st3]
    be.set_hierarchy_probs([st1, st2, st3])
    assert_close_enough(st1.belief, 1-0.35)
    assert_close_enough(st2.belief, 1-0.35*0.35)

```
