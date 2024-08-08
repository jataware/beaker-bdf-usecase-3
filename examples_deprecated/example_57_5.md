# Description
Testing the belief engine with a combination of evidence types including an assertion.

# Code
```
from copy import deepcopy
import pytest
from indra.statements import Evidence, Agent, Phosphorylation
from indra.belief import BeliefEngine, load_default_probs

default_probs = load_default_probs()
ev1 = Evidence(source_api='reach')
ev2 = Evidence(source_api='trips')

def test_prior_prob_assertion():
    be = BeliefEngine()
    st = Phosphorylation(None, Agent('a'),
                         evidence=[ev1, deepcopy(ev1), ev2, ev3])
    assert st.belief == 1
    be.set_prior_probs([st])

```
