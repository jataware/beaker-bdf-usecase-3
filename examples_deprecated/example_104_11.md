# Description
Test for `process_file` method to process 'test_Inhibition.csxml' data file.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
os.path import join, dirname
indra.sources.medscan.api import process_file
indra.statements import Inhibition

def test_inhibition():
    fname = os.path.join(data_folder, 'test_Inhibition.csxml')
    mp = process_file(fname, None)

    statements = mp.statements
    assert len(statements) == 1

    s0 = statements[0]
    assert type(s0) == Inhibition
    assert repr(s0.subj) == 'DNMT3A(mods: (methylation, R, 882))'

```
