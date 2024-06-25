# Description
Testing the belief engine's ability to set prior probabilities for two pieces of evidence from the same source.

# Code
```
from copy import deepcopy
import pytest
from indra.statements import Evidence, Agent, Phosphorylation
from indra.belief import BeliefEngine, load_default_probs

default_probs = load_default_probs()

def test_prior_prob_two_same():
    be = BeliefEngine()
    prob = 1 - (default_probs['rand']['reach']**2 +
                default_probs['syst']['reach'])
    st = Phosphorylation(None, Agent('a'), evidence=[ev1, deepcopy(ev1)])
    assert st.belief == 1
    be.set_prior_probs([st])

```
