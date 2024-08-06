# Description
Process Signor interaction data from a local CSV file. The function `process_from_file` reads Signor interaction data and optionally Signor complexes data from specified CSV files, and returns a `SignorProcessor` containing Statements extracted from this data.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
import sys
import logging
from io import StringIO, BytesIO
from collections import namedtuple
from .processor import SignorProcessor
from indra.util import read_unicode_csv, read_unicode_csv_fileobj

logger = logging.getLogger(__name__)

_signor_fields = [
    'ENTITYA', 'TYPEA', 'IDA', 'DATABASEA', 'ENTITYB', 'TYPEB', 'IDB', 'DATABASEB', 'EFFECT', 'MECHANISM', 'RESIDUE', 'SEQUENCE', 'TAX_ID', 'CELL_DATA', 'TISSUE_DATA', 'MODULATOR_COMPLEX', 'TARGET_COMPLEX', 'MODIFICATIONA', 'MODASEQ', 'MODIFICATIONB', 'MODBSEQ', 'PMID', 'DIRECT', 'NOTES', 'ANNOTATOR', 'SENTENCE', 'SCORE', 'SIGNOR_ID'
]


def process_from_file(signor_data_file, signor_complexes_file=None,
                      delimiter='\t'):
    """Process Signor interaction data from CSV files.

    Parameters
    ----------
    signor_data_file : str
        Path to the Signor interaction data file in CSV format.
    signor_complexes_file : Optional[str]
        Path to the Signor complexes data in CSV format. If specified,
        Signor complexes will not be expanded to their constitutents.
    delimiter : Optional[str]
        The delimiter used in the data file. Older data files use ;
        as a delimiter whereas more recent ones use tabs.

    Returns
    -------
    indra.sources.signor.SignorProcessor
        SignorProcessor containing Statements extracted from the Signor data.
    """
    # Get generator over the CSV file
    data_iter = read_unicode_csv(signor_data_file, delimiter=delimiter,
                                 skiprows=1)
    complexes_iter = None
    if signor_complexes_file:
        complexes_iter = read_unicode_csv(signor_complexes_file, delimiter=';',
                                          skiprows=1)
    else:
        logger.warning('Signor complex mapping file not provided, Statements '
                       'involving complexes will not be expanded to members.')

```
