# Description
Testing the BayesianScorer's ability to update belief probabilities based on new evidence.

# Code
```
copy import deepcopy
pytest
indra.statements import Evidence

def test_bayesian_scorer():
    prior_counts = {'hume': [3, 1]}
    subtype_counts = {'eidos': {'rule1': [2, 2], 'rule2': [1, 4]}}
    scorer = BayesianScorer(prior_counts, subtype_counts)
    # Check initial probability assignment
    assert scorer.prior_probs['rand']['hume'] == 0.2
    assert scorer.prior_probs['syst']['hume'] == 0.05
    assert scorer.subtype_probs['eidos']['rule1'] == 0.45
    assert scorer.subtype_probs['eidos']['rule2'] == 0.75
    # Now try to do some updates
    scorer.update_counts({'hume': [0, 2]}, {})
    assert scorer.prior_counts['hume'] == [3, 3]
    scorer.update_counts({}, {'eidos': {'rule1': [6, 0]}})
    assert scorer.subtype_counts['eidos']['rule1'] == [8, 2]
    # Now check that the probabilities are up to date
    assert scorer.prior_probs['rand']['hume'] == 0.45
    assert scorer.prior_probs['syst']['hume'] == 0.05
    assert_close_enough(scorer.subtype_probs['eidos']['rule1'],
                        0.15)

```
