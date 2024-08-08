# Description
Test for `process_file` method to process 'test_MolSynthesis-negative.csxml' data file.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
os.path import join, dirname
indra.sources.medscan.api import process_file
indra.statements import DecreaseAmount

def test_molsynthesis_negative():
    fname = os.path.join(data_folder, 'test_MolSynthesis-negative.csxml')
    mp = process_file(fname, None)

    statements = mp.statements
    assert len(statements) == 1

    s0 = statements[0]
    assert isinstance(s0, DecreaseAmount)

    assert s0.subj.db_refs == {'HGNC': '9070', 'TEXT': 'pleckstrin',
                               'UP': 'P08567'}

```
