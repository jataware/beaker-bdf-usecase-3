# Description
Instantiate and use CountsScorer for fitting and making predictions on statements

# Code
```
import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from indra.belief.skl import CountsScorer

# Load data files
with open(test_stmt_path, 'rb') as f:

def test_fit_stmts_predict_stmts():
    lr = LogisticRegression()
    source_list = ['reach', 'sparser', 'signor']
    cw = CountsScorer(lr, source_list)
    cw.fit(test_stmts, y_arr_stmts)
    probs = cw.predict_proba(test_stmts)
    assert probs.shape == (len(test_stmts), 2), \
        'prediction results should have dimension (# stmts, # classes)'
    log_probs = cw.predict_log_proba(test_stmts)
    assert log_probs.shape == (len(test_stmts), 2), \
        'prediction results should have dimension (# stmts, # classes)'
    preds = cw.predict(test_stmts)
    assert preds.shape == (len(test_stmts),), \

```
