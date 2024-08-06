# Description
Test for `process_file` method to process 'test_Protein_Mutation.csxml' data file.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
os.path import join, dirname
indra.sources.medscan.api import process_file
indra.statements import Complex

def test_protein_mutation():
    fname = os.path.join(data_folder, 'test_Protein_Mutation.csxml')
    mp = process_file(fname, None)

    statements = mp.statements
    assert len(statements) == 1

    s0 = statements[0]
    assert isinstance(s0, Complex)

    members = s0.members
    assert len(members) == 2
    m0 = members[0]
    m1 = members[1]

    assert m0.db_refs == {'HGNC': '7910', 'UP': 'P06748', 'TEXT': 'NPM1'}
    assert len(m0.mods) == 0
    assert len(m0.mutations) == 0

    assert m1.db_refs == {'HGNC': '25994', 'UP': 'Q08J23', 'TEXT': 'NSUN2'}
    assert len(m1.mods) == 0
    assert len(m1.mutations) == 1
    mut = m1.mutations[0]
    assert mut.position == '139'
    assert mut.residue_from == 'S'

```
