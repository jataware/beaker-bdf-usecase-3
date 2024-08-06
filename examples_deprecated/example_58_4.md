# Description
Setup belief engine and return parameters for testing belief updates

# Code
```
import pickle
import numpy as np
from copy import copy
from sklearn.linear_model import LogisticRegression
from indra.belief import BeliefEngine
from indra.belief.skl import CountsScorer

# Load data files
with open(test_stmt_cur_path, 'rb') as f:
    test_stmts_cur, y_arr_stmts_cur = pickle.load(f)


def setup_belief(include_more_specific=False):
    # Make a model
    lr = LogisticRegression()
    # Get all the sources
    source_list = CountsScorer.get_all_sources(test_stmts_cur)
    cs = CountsScorer(lr, source_list,
                      include_more_specific=include_more_specific)
    # Train on curated stmt data
    if include_more_specific:
        extra_evidence = [[ev for supp in stmt.supports
                              for ev in supp.evidence]
                          for stmt in test_stmts_cur]
    else:
        extra_evidence = None
    # Fit with extra evidence, if any
    cs.fit(test_stmts_cur, y_arr_stmts_cur, extra_evidence)
    # Run predictions on test statements without extra evidence to get prior
    # probs
    probs = cs.predict_proba(test_stmts_cur)[:, 1]
    # Now check if we get these same beliefs set on the statements when we
    # run with the belief engine:
    # Get scorer and belief engine instances for trained model
    be = BeliefEngine(scorer=cs)
    # Make a shallow copy of the test stmts so that we don't change beliefs
    # of the global instances as a side-effect of this test
    test_stmts_copy = copy(test_stmts_cur)

```
