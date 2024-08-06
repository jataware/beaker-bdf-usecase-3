# Description
Test for `process_file` method to process 'test_ExpressionControl_positive.csxml' data file.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
os.path import join, dirname
indra.sources.medscan.api import process_file

def test_expressioncontrol_positive():
    fname = os.path.join(data_folder, 'test_ExpressionControl_positive.csxml')
    mp = process_file(fname, None)

    statements = mp.statements
    assert len(statements) == 2

    s0 = statements[0]

    assert s0.subj.db_refs == {'TEXT': 'hypoxia'}
    assert s0.obj.db_refs == {'HGNC': '3415', 'TEXT': 'erythropoietin',

```
