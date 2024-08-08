# Description
Demonstrates how to use the `CountsScorer` class to score statements using a logistic regression model.

# Code
```
import logging
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from indra.statements import Statement
from indra.belief import BeliefEngine

# Assuming `stmts` is a list of statements and `y_arr` is the corresponding array of class labels

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()
all_stmt_sources = CountsScorer.get_all_sources(stmts)
scorer = CountsScorer(clf, all_stmt_sources, use_stmt_type=True,
                      use_num_pmids=True)
scorer.fit(stmts, y_arr)
be = BeliefEngine(scorer)
be.set_hierarchy_probs(stmts)

```
