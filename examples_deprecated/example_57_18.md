# Description
Testing the belief engine's handling of negated evidence through the set_prior_probs method.

# Code
```
from copy import deepcopy
import pytest
from indra.statements import Evidence, Agent, Phosphorylation
from indra.belief import BeliefEngine, load_default_probs, SimpleScorer


def test_negative_evidence():
    prior_probs = {'rand': {'new_source': 0.1},
                   'syst': {'new_source': 0.05}}
    getev = lambda x: Evidence(source_api='new_source',
                               epistemics={'negated': x})
    evs1 = [getev(x) for x in [True, True, False]]
    evs2 = [getev(x) for x in [False, False, False]]
    evs3 = [getev(x) for x in [True, True, True]]
    stmts = [Phosphorylation(None, Agent('a'), evidence=e)
             for e in [evs1, evs2, evs3]]
    scorer = SimpleScorer(prior_probs)
    engine = BeliefEngine(scorer)
    engine.set_prior_probs(stmts)
    pr = prior_probs['rand']['new_source']
    ps = prior_probs['syst']['new_source']
    assert_close_enough(stmts[0].belief, ((1-pr)-ps)*(1-((1-pr*pr)-ps)))
    assert_close_enough(stmts[1].belief, (1-pr*pr*pr)-ps)

```
