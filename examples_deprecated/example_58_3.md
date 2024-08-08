# Description
Check the positions of required columns in dataframe and attempt to convert to matrix using CountsScorer

# Code
```
import pytest
import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression
from indra.belief.skl import CountsScorer

# Load data files

def test_check_df_cols_err():
    """Drop a required column and make sure we get a ValueError."""
    with pytest.raises(ValueError):
        lr = LogisticRegression()
        source_list = ['reach', 'sparser', 'signor']
        cw = CountsScorer(lr, source_list)

```
