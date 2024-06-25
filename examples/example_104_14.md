# Description
Test for `process_file` method to process 'test_Protein_MethSite.csxml' data file.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
os.path import join, dirname
indra.sources.medscan.api import process_file
indra.statements import Complex

def test_protein_methsite():
    fname = os.path.join(data_folder, 'test_Protein_MethSite.csxml')
    mp = process_file(fname, None)

    statements = mp.statements
    assert len(statements) == 1

    s0 = statements[0]
    assert isinstance(s0, Complex)

    members = s0.members
    assert len(members) == 2
    m0 = members[0]
    m1 = members[1]

    assert m0.db_refs == {'HGNC': '2978', 'UP': 'Q9Y6K1', 'TEXT': 'DNMT3A'}
    assert len(m0.mutations) == 0
    assert len(m0.mods) == 1
    mod = m0.mods[0]
    assert mod.mod_type == 'methylation'
    assert mod.residue == 'R'

```
