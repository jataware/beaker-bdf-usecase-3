# Description
Testing the sampling of statements based on their belief probabilities.

# Code
```
from copy import deepcopy
import pytest
from indra.statements import Evidence, Agent, Phosphorylation
from indra.belief import BeliefEngine, load_default_probs, sample_statements


def test_sample_statements():
    st1 = Phosphorylation(Agent('B'), Agent('A1'))
    st2 = Phosphorylation(None, Agent('A1'))
    st3 = Phosphorylation(None, Agent('A'))
    st1.supported_by = [st2, st3]
    st2.supported_by = [st3]
    st2.supports = [st1]
    st3.supports = [st1, st2]
    st1.belief = 0.8
    st2.belief = 0.6
    st3.belief = 0.5
    stmts = sample_statements([st1, st2, st3], seed=10)
    # Random numbers are 0.77132064  0.02075195  0.63364823 with this seed
    assert len(stmts) == 2
    assert st1 in stmts
    assert st2 in stmts

```
