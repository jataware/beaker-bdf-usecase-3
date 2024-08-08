# Description
Testing the default probabilities are overridden using the constructor argument for BeliefEngine.

# Code
```
from copy import deepcopy
import pytest
from indra.statements import Evidence, Agent, Phosphorylation
from indra.belief import BeliefEngine, load_default_probs, SimpleScorer


def test_default_probs_override():
    """Make sure default probs are overriden by constructor argument."""
    prior_probs = {'rand': {'assertion': 0.5}}
    scorer = SimpleScorer(prior_probs)

    be = BeliefEngine(scorer)
    for err_type in ('rand', 'syst'):
        for k, v in scorer.prior_probs[err_type].items():
            if err_type == 'rand' and k == 'assertion':
                assert v == 0.5
            else:

```
