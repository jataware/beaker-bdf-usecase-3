# Description
Test for `process_file` method to process 'test_Phosphorylate.csxml' data file.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
os.path import join, dirname
indra.sources.medscan.api import process_file
indra.statements import Phosphorylation

def test_phosphorylate():
    fname = os.path.join(data_folder, 'test_Phosphorylate.csxml')
    mp = process_file(fname, None)

    statements = mp.statements
    assert len(statements) == 1

    s0 = statements[0]
    assert isinstance(s0, Phosphorylation)

    assert s0.enz.db_refs == {'GO': 'GO:0005610', 'FPLX': 'Laminin_332',
                              'TEXT': 'IKK alpha'}
    assert s0.enz.name == 'Laminin_332'  # agent name is FPLX when available

```
