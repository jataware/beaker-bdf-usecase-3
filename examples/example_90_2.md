# Description
Test processing HPRD post-translational modifications (PTMs) from flat files.

# Code
```
from os.path import join, abspath, dirname
import pytest
from indra.statements import Phosphorylation
from indra.sources import hprd

test_dir = join(abspath(dirname(__file__)), 'hprd_tests_data')

def test_process_ptms():
    ptm_file = join(test_dir, 'POST_TRANSLATIONAL_MODIFICATIONS.txt')
    seq_file = join(test_dir, 'PROTEIN_SEQUENCES.txt')
    hp = hprd.process_flat_files(id_file, ptm_file=ptm_file, seq_file=seq_file)
    assert isinstance(hp, hprd.HprdProcessor)
    assert isinstance(hp.statements, list)
    assert len(hp.statements) == 13
    s0 = hp.statements[0]
    assert isinstance(s0, Phosphorylation)
    assert s0.enz.name == 'MAPK1'
    assert s0.enz.db_refs == {'UP': 'P28482', 'HGNC': '6871', 'EGID': '5594',
                              'REFSEQ_PROT': 'NP_002736.3'}
    assert s0.sub.name == 'TCF3'
    assert s0.sub.db_refs == {'UP': 'P15923', 'HGNC': '11633', 'EGID': '6929',
                              'REFSEQ_PROT': 'NP_003191.1'}
    assert s0.residue == 'T'
    assert s0.position == '355'
    assert len(s0.evidence) == 1
    assert s0.evidence[0].pmid == '14592976'
    assert s0.evidence[0].source_api == 'hprd'
    assert s0.evidence[0].annotations['evidence'] == ['in vivo']
    assert s0.evidence[0].annotations['site_motif'] == \
                    {'motif': 'NFSSSPSTPVGSPQG', 'respos': 8,

```
