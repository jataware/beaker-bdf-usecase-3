# Description
Test for `process_file` method to process 'test_ExpressionControl_negative.csxml' data file.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
os.path import join, dirname
indra.sources.medscan.api import process_file
indra.statements import DecreaseAmount

def test_expressioncontrol_negative():
    fname = os.path.join(data_folder, 'test_ExpressionControl_negative.csxml')
    mp = process_file(fname, None)

    statements = mp.statements
    assert len(statements) == 1

    s0 = statements[0]
    assert isinstance(s0, DecreaseAmount)
    assert s0.subj.db_refs == {'CHEBI': 'CHEBI:6700', 'TEXT': 'matrine'}
    assert s0.obj.db_refs == {'HGNC': '6364',
                              'TEXT': 'PSA and androgen receptor',

```
