# Description
Test for `process_file` method to process 'test_Protein_PhosphoSite.csxml' data file.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
os.path import join, dirname
indra.sources.medscan.api import process_file
indra.statements import DecreaseAmount

def test_protein_phosphosite():
    fname = os.path.join(data_folder, 'test_Protein_PhosphoSite.csxml')
    mp = process_file(fname, None)

    statements = mp.statements
    assert len(statements) == 1

    s0 = statements[0]
    assert isinstance(s0, DecreaseAmount)

    subj = s0.subj
    assert subj.db_refs == {'HGNC': '115', 'UP': 'P53396', 'TEXT': 'ACLY'}
    assert len(subj.mutations) == 0
    assert len(subj.mods) == 1
    mod = subj.mods[0]
    assert mod.residue == 'S'
    assert mod.position == '455'
    assert mod.mod_type == 'phosphorylation'

    obj = s0.obj
    assert obj.db_refs == {'CHEBI': 'CHEBI:15351', 'TEXT': 'acetyl-CoA'}
    assert len(obj.mutations) == 0

```
