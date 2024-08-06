# Description
Testing the belief engine's ability to set prior probabilities for two different sources of evidence.

# Code
```
from copy import deepcopy
import pytest
from indra.statements import Evidence, Agent, Phosphorylation
from indra.belief import BeliefEngine, load_default_probs

default_probs = load_default_probs()
ev1 = Evidence(source_api='reach')

def test_prior_prob_two_different():
    be = BeliefEngine()
    prob = 1 - (default_probs['rand']['reach'] +
                default_probs['syst']['reach']) * \
               (default_probs['rand']['trips'] +
                default_probs['syst']['trips'])
    st = Phosphorylation(None, Agent('a'), evidence=[ev1, ev2])
    assert st.belief == 1
    be.set_prior_probs([st])

```
