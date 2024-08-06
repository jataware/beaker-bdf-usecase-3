# Description
Test for `process_file` method to process 'test_Activation.csxml' data file.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
os.path import join, dirname
indra.sources.medscan.api import process_file
indra.statements import Activation

def test_activation():
    fname = os.path.join(data_folder, 'test_Activation.csxml')
    mp = process_file(fname, None)

    statements = mp.statements
    assert len(statements) == 1

    s0 = statements[0]
    assert type(s0) == Activation
    assert s0.subj.name == 'Laminin_332'

```
