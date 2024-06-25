# Description
Process an HPRD data tar.gz file and extract INDRA Statements using `process_archive` function.

# Code
```
import tarfile
import pandas as pd
from indra.sources.hprd.processor import HprdProcessor
from protmapper.uniprot_client import load_fasta_sequences, load_fasta_sequence_lines

_hprd_id_cols = ['HPRD_ID', 'HGNC_SYMBOL', 'REFSEQ_GENE', 'REFSEQ_PROTEIN', 'EGID', 'OMIM', 'UNIPROT', 'NAME']
_cplx_cols = ['CPLX_ID', 'HPRD_ID', 'HGNC_SYMBOL', 'REFSEQ_PROTEIN', 'EVIDENCE', 'PMIDS']
_ptm_cols = ['HPRD_ID', 'HGNC_SYMBOL', 'HPRD_ISOFORM', 'REFSEQ_PROTEIN', 'POSITION', 'RESIDUE', 'ENZ_HGNC_SYMBOL', 'ENZ_HPRD_ID', 'MOD_TYPE', 'EVIDENCE', 'PMIDS']
_ppi_cols = ['HGNC_SYMBOL_A', 'HPRD_ID_A', 'REFSEQ_PROTEIN_A', 'HGNC_SYMBOL_B', 'HPRD_ID_B', 'REFSEQ_PROTEIN_B', 'EVIDENCE', 'PMIDS']
file_mappings = {
    'id_mappings_file': 'HPRD_ID_MAPPINGS.txt',
    'complexes_file': 'PROTEIN_COMPLEXES.txt',
    'ptm_file': 'POST_TRANSLATIONAL_MODIFICATIONS.txt',
    'ppi_file': 'BINARY_PROTEIN_PROTEIN_INTERACTIONS.txt',
    'seq_file': 'PROTEIN_SEQUENCES.txt'

def process_archive(fname):
    """Get INDRA Statements from HPRD data in a single tar.gz file.

    The latest release, HPRD_FLAT_FILES_041310.tar.gz can be downloaded from
    http://hprd.org/download after registration.

    Parameters
    ----------
    fname : str
        Path to HPRD tar.gz file.

    Returns
    -------
    HprdProcessor
        An HprdProcessor object which contains a list of extracted INDRA
        Statements in its statements attribute.
    """
    with tarfile.open(fname, "r:gz") as fh:
        prefix = fh.next().name.split('/')[0]
        files = {k: fh.extractfile(prefix + '/' + v) for k, v in
                 file_mappings.items()}

```
