# Description
Testing the belief engine's ability to integrate evidence from multiple sources and the same source with the same piece of evidence.

# Code
```
from copy import deepcopy
import pytest
from indra.statements import Evidence, Agent, Phosphorylation
from indra.belief import BeliefEngine, load_default_probs

default_probs = load_default_probs()
ev1 = Evidence(source_api='reach')

def test_prior_prob_one_two():
    be = BeliefEngine()
    prob = 1 - (default_probs['rand']['reach']**2 +
                default_probs['syst']['reach']) * \
               (default_probs['rand']['trips'] +
                default_probs['syst']['trips'])
    st = Phosphorylation(None, Agent('a'), evidence=[ev1, deepcopy(ev1), ev2])
    assert st.belief == 1
    be.set_prior_probs([st])

```
