# Description
Test for `process_file` method to process 'test_Binding.csxml' data file.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
os.path import join, dirname
indra.sources.medscan.api import process_file
indra.statements import Complex

def test_binding():
    fname = os.path.join(data_folder, 'test_Binding.csxml')
    mp = process_file(fname, None)

    statements = mp.statements
    assert len(statements) == 1

    s0 = statements[0]
    assert isinstance(s0, Complex)
    members = s0.members
    assert len(members) == 2
    m0 = members[0]
    m1 = members[1]

    assert m0.db_refs == {'HGNC': '7664', 'TEXT': 'Both Nck and Grb4',
                          'UP': 'P16333'}

```
