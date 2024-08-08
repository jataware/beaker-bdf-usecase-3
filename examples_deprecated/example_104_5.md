# Description
Test for `process_file` method to process 'test_MolSynthesis-positive.csxml' data file.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
os.path import join, dirname
indra.sources.medscan.api import process_file
indra.statements import IncreaseAmount

def test_molsynthesis_positive():
    fname = os.path.join(data_folder, 'test_MolSynthesis-positive.csxml')
    mp = process_file(fname, None)

    statements = mp.statements
    assert len(statements) == 1

    s0 = statements[0]
    assert isinstance(s0, IncreaseAmount)

    assert s0.subj.db_refs == {'HGNC': '19260', 'TEXT': 'BLT2',
                               'UP': 'Q9NPC1'}

```
