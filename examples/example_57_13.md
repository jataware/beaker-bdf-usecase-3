# Description
Testing the default probabilities are extended using the constructor argument for the BeliefEngine.

# Code
```
from copy import deepcopy
import pytest
from indra.statements import Evidence, Agent, Phosphorylation
from indra.belief import BeliefEngine, load_default_probs, SimpleScorer


def test_default_probs_extend():
    """Make sure default probs are extended by constructor argument."""
    prior_probs = {'rand': {'new_source': 0.1},
                   'syst': {'new_source': 0.05}}
    scorer = SimpleScorer(prior_probs)

    be = BeliefEngine(scorer)
    for err_type in ('rand', 'syst'):
        assert 'new_source' in scorer.prior_probs[err_type]
        for k, v in scorer.prior_probs[err_type].items():
            if err_type == 'rand' and k == 'new_source':
                assert v == 0.1
            elif err_type == 'syst' and k == 'new_source':
                assert v == 0.05
            else:

```
