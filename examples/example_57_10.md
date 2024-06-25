# Description
Testing the default probabilities are set using an empty BeliefEngine constructor.

# Code
```
from copy import deepcopy
import pytest
from indra.statements import Evidence, Agent, Phosphorylation
from indra.belief import BeliefEngine, load_default_probs


def test_default_probs():
    """Make sure default probs are set with empty constructor."""
    be = BeliefEngine()
    for err_type in ('rand', 'syst'):
        for k, v in default_probs[err_type].items():

```
