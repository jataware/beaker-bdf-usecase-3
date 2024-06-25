# Description
Process chemical-gene interactions from two TSV files and validate the statements.

# Code
```
os
indra.sources.gnbr.processor import *
indra.sources.gnbr.api as api

def test_process_chemical_gene():
    test_path1: str = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   'gnbr_chemical_gene_part1_test.tsv')
    test_path2: str = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   'gnbr_chemical_gene_part2_test.tsv')
    gp = api.process_chemical_gene(test_path1, test_path2)
    assert len(gp.statements) != 0
    assert isinstance(gp, GnbrProcessor)
    assert gp.first_type == 'chemical'
    assert gp.second_type == 'gene'
    assert isinstance(gp.statements[0], Activation)
    assert isinstance(gp.statements[1], Inhibition)
    assert isinstance(gp.statements[2], Complex)
    assert isinstance(gp.statements[3], DecreaseAmount)

```
