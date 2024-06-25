# Description
Instantiate and use CountsScorer to convert statements to a matrix

# Code
```
import random
import pickle
import numpy as np
import pandas as pd
from collections import defaultdict
from sklearn.linear_model import LogisticRegression
from indra.sources import signor
from indra.belief.skl import CountsScorer

# Load data files
with open(test_stmt_path, 'rb') as f:
    test_stmts, y_arr_stmts = pickle.load(f)
with open(test_stmt_cur_path, 'rb') as f:
    test_stmts_cur, y_arr_stmts_cur = pickle.load(f)

def test_stmts_to_matrix():
    """Check that all source_apis in training data are in source list."""
    lr = LogisticRegression()
    source_list = ['reach', 'sparser', 'signor']
    cw = CountsScorer(lr, source_list)
    x_arr = cw.stmts_to_matrix(test_stmts)
    assert isinstance(x_arr, np.ndarray), 'x_arr should be a numpy array'
    assert x_arr.shape == (len(test_stmts), len(source_list)), \
            'stmt matrix dimensions should match test stmts'
    assert set(x_arr.sum(axis=0)) == set([0, 0, len(test_stmts)]), \
           'Signor col should be 1 in every row, other cols 0.'
    # Try again with statement type
    cw = CountsScorer(lr, source_list, use_stmt_type=True)
    num_types = len(cw.stmt_type_map)
    x_arr = cw.stmts_to_matrix(test_stmts)
    assert x_arr.shape == (len(test_stmts), len(source_list) + num_types), \
        'matrix should have a col for sources and other cols for every ' \

```
