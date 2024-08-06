# Description
Test processing HPRD protein-protein interactions (PPIs) from flat files.

# Code
```
from os.path import join, abspath, dirname
import pytest
from indra.statements import Complex
from indra.sources import hprd

test_dir = join(abspath(dirname(__file__)), 'hprd_tests_data')

def test_process_ppis():
    ppi_file = join(test_dir, 'BINARY_PROTEIN_PROTEIN_INTERACTIONS.txt')
    hp = hprd.process_flat_files(id_file, ppi_file=ppi_file)
    assert isinstance(hp, hprd.HprdProcessor)
    assert isinstance(hp.statements, list)
    assert len(hp.statements) == 5
    s0 = hp.statements[0]
    assert isinstance(s0, Complex)
    assert len(s0.members) == 2
    assert set([ag.name for ag in s0.members]) == set(['ITGA7', 'CHRNA1'])
    assert s0.members[0].db_refs == \
            {'HGNC': '6143', 'UP': 'Q13683', 'EGID': '3679',
             'REFSEQ_PROT': 'NP_001138468.1'}
    assert s0.members[1].db_refs == \
            {'HGNC': '1955', 'UP': 'P02708', 'EGID': '1134',
             'REFSEQ_PROT': 'NP_001034612.1'}
    assert len(s0.evidence) == 1
    assert s0.evidence[0].pmid == '10910772'
    assert s0.evidence[0].source_api == 'hprd'
    assert s0.evidence[0].annotations['evidence'] == ['in vivo']
    assert s0.evidence[0].source_id == ('http://hprd.org/interactions?'
                                     'hprd_id=02761&isoform_id=02761_1'

```
