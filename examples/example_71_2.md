# Description
Example of processing a TSV file with CTDChemicalGeneProcessor to generate statements and make assertions about them.

# Code
```
import os
from indra.statements import *
from indra.sources import ctd


def test_chemical_gene():
    fname = os.path.join(HERE, 'ctd_chem_gene_20522546.tsv')
    cp = ctd.process_tsv(fname, 'chemical_gene')
    assert len(cp.statements) == 3, cp.statements
    assert isinstance(cp.statements[0], Dephosphorylation)
    assert cp.statements[0].enz.name == 'wortmannin'
    assert isinstance(cp.statements[1], Dephosphorylation)
    assert cp.statements[1].enz.name == 'YM-254890'
    assert isinstance(cp.statements[2], Phosphorylation)

```
