# Description
Test for `process_file` method to process 'test_Dephosphorylate.csxml' data file.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
os.path import join, dirname
indra.sources.medscan.api import process_file
indra.statements import Dephosphorylation

def test_dephosphorylate():
    fname = os.path.join(data_folder, 'test_Dephosphorylate.csxml')
    mp = process_file(fname, None)

    statements = mp.statements
    assert len(statements) == 1

    s0 = statements[0]
    assert isinstance(s0, Dephosphorylation)

    assert s0.enz.db_refs == {'HGNC': '30579', 'TEXT': 'Slingshot-1 (SSH1',
                              'UP': 'Q8WYL5'}
    assert s0.sub.db_refs == {'HGNC': '1874', 'TEXT': 'cofilin',

```
