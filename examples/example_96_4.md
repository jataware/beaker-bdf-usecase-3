# Description
Test the conversion of IndraNetAssembler output to a pandas DataFrame and inclusion of extra columns.

# Code
```
import numpy as np
import pandas as pd
import networkx as nx
from indra.statements import *
from indra.assemblers.indranet.net import default_sign_dict
from indra.assemblers.indranet import IndraNetAssembler, IndraNet

ev1 = Evidence(pmid='1')
ev2 = Evidence(pmid='2')
ev3 = Evidence(pmid='3')
st1 = Activation(Agent('a', db_refs={'HGNC': '1'}), Agent('b'), evidence=[ev1])
st2 = Inhibition(Agent('a', db_refs={'HGNC': '1'}), Agent('c'), evidence=[ev1, ev2, ev3])
st2.belief = 0.76
st3 = Activation(Agent('b'), Agent('d'))
st4 = ActiveForm(Agent('e'), None, True)
st5 = Complex([Agent('c'), Agent('f'), Agent('g')])
st6 = Complex([Agent('h'), Agent('i'), Agent('j'), Agent('b')])

def test_make_df():
    ia = IndraNetAssembler([st1, st2, st3, st4, st5, st6, st9])
    df = ia.make_df()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 10
    assert set(df.columns) == {
        'agA_name', 'agB_name', 'agA_ns', 'agA_id', 'agB_ns', 'agB_id',
        'stmt_type', 'evidence_count', 'stmt_hash', 'belief', 'source_counts',
        'initial_sign', 'residue', 'position'}
    assert df.residue.isna().sum() == 9  # Check that all but one row is NaN
    assert df.position.isna().sum() == 9  # Check that all but one row is NaN
    # Extra column
    df2 = ia.make_df(extra_columns=[
        ('stmt_type_upper',
         lambda stmt: type(stmt).__name__.upper())])
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 10
    assert set(df2.columns) - set(df.columns) == {'stmt_type_upper'}

```
