# Description
Testing the belief engine's ability to set prior probabilities for a single source of evidence.

# Code
```
from copy import deepcopy
import pytest
from indra.statements import Evidence, Agent, Phosphorylation
from indra.belief import BeliefEngine, load_default_probs

default_probs = load_default_probs()

def test_prior_prob_one():
    be = BeliefEngine()
    prob = 1 - (default_probs['rand']['reach'] +
                default_probs['syst']['reach'])
    st = Phosphorylation(None, Agent('a'), evidence=[ev1])
    assert st.belief == 1
    be.set_prior_probs([st])

```
