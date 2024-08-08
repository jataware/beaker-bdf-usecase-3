# Description
Testing the ability to score a single statement using a custom SimpleScorer.

# Code
```
from copy import deepcopy
import pytest
from indra.statements import Evidence, Agent, Phosphorylation
from indra.belief import BeliefEngine, load_default_probs, SimpleScorer

default_probs = load_default_probs()
ev1 = Evidence(source_api='reach')

def test_score_statement():
    """Check that we can correctly score a single statement."""
    prior_probs = {'rand': {'reach': 0.1, 'trips': 0.2},
                   'syst': {'reach': 0,   'trips': 0}}

    scorer = SimpleScorer(prior_probs)
    # ev1 is from "reach"
    st1 = Phosphorylation(None, Agent('a'), evidence=[ev1])
    belief = scorer.score_statement(st1)
    assert belief == 0.9
    # try extra_evidence empty list:
    belief = scorer.score_statement(st1, extra_evidence=[])
    assert belief == 0.9
    # Now we try extra_evidence from trips.
    # Expected result is 1 - (0.1 * 0.2) = 0.98
    belief = scorer.score_statement(st1, extra_evidence=[ev2])

```
