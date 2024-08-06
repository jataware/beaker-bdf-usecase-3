# Description
Testing the belief engine's hierarchical probabilities with a hierarchy involving more supporting statements.

# Code
```
from copy import deepcopy
import pytest
from indra.statements import Evidence, Agent, Phosphorylation
from indra.belief import BeliefEngine, load_default_probs

default_probs = load_default_probs()
ev1 = Evidence(source_api='reach')
ev2 = Evidence(source_api='trips')

def test_hierarchy_probs4():
    be = BeliefEngine()
    st1 = Phosphorylation(None, Agent('a'), evidence=[ev1])
    st2 = Phosphorylation(None, Agent('b'), evidence=[ev2])
    st3 = Phosphorylation(None, Agent('c'), evidence=[deepcopy(ev1)])
    st4 = Phosphorylation(None, Agent('d'), evidence=[deepcopy(ev1)])
    st4.supports = [st1, st2, st3]
    st3.supports = [st1]
    st2.supports = [st1]
    st1.supported_by = [st2, st3, st4]
    st2.supported_by = [st4]
    st3.supported_by = [st4]
    be.set_hierarchy_probs([st1, st2, st3, st4])
    assert_close_enough(st1.belief, 1-0.35)
    assert_close_enough(st2.belief, 1-0.35*0.35)
    assert_close_enough(st3.belief, 1-(0.05 + 0.3*0.3))

```
