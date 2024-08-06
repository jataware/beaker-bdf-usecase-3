# Description
Testing that setting prior probabilities raises an exception when using an unknown evidence source.

# Code
```
from copy import deepcopy
import pytest
from indra.statements import Evidence, Agent, Phosphorylation
from indra.belief import BeliefEngine, load_default_probs


def test_check_prior_probs():
    with pytest.raises(Exception):
        be = BeliefEngine()
        st = Phosphorylation(None, Agent('ERK'),
                             evidence=[Evidence(source_api='xxx')])

```
