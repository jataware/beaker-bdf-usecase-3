# Description
Test for detecting modification site and residue in a modification event using `process_file` method.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
os.path import join, dirname
indra.sources.medscan.api import process_file

def test_modification_site():
    # Can we detect the modification site and residue in a modification
    # event?
    fname = os.path.join(data_folder, 'test_modification_site.csxml')
    mp = process_file(fname, None)

    statements = mp.statements
    assert len(statements) == 1

    s0 = statements[0]
    assert s0.residue == 'K'

```
