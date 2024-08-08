# Description
Process gene-disease interactions from two TSV files and validate the statements.

# Code
```
os
indra.sources.gnbr.processor import *
indra.sources.gnbr.api as api

def test_process_gene_disease():
    test_path1: str = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   'gnbr_gene_disease_part1_test.tsv')
    test_path2: str = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   'gnbr_gene_disease_part2_test.tsv')
    gp = api.process_gene_disease(test_path1, test_path2)
    assert len(gp.statements) != 0
    assert isinstance(gp, GnbrProcessor)
    assert gp.first_type == 'gene'
    assert gp.second_type == 'disease'
    assert isinstance(gp.statements[0], Inhibition)
    assert isinstance(gp.statements[1], Activation)

```
