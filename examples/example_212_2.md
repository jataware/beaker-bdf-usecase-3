# Description
Process Signor interaction data from the web. The function `process_from_web` downloads the latest interaction and complex data directly from the Signor website without an intermediate local file, and returns a `SignorProcessor` containing Statements extracted from this data.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
import sys
import logging
import requests
from io import StringIO, BytesIO
from collections import namedtuple
from .processor import SignorProcessor
from indra.util import read_unicode_csv, read_unicode_csv_fileobj

logger = logging.getLogger(__name__)

_signor_fields = [
    'ENTITYA', 'TYPEA', 'IDA', 'DATABASEA', 'ENTITYB', 'TYPEB', 'IDB', 'DATABASEB', 'EFFECT', 'MECHANISM', 'RESIDUE', 'SEQUENCE', 'TAX_ID', 'CELL_DATA', 'TISSUE_DATA', 'MODULATOR_COMPLEX', 'TARGET_COMPLEX', 'MODIFICATIONA', 'MODASEQ', 'MODIFICATIONB', 'MODBSEQ', 'PMID', 'DIRECT', 'NOTES', 'ANNOTATOR', 'SENTENCE', 'SCORE', 'SIGNOR_ID'
]

_SignorRow_ = namedtuple('SignorRow', _signor_fields)

def _handle_response(res, delimiter, fname=None):
    if res.status_code == 200:
        if sys.version_info[0] < 3:
            csv_io = BytesIO(res.content)
            if fname:
                with open(fname, 'wb') as fh:
                    fh.write(res.content)
        else:
            csv_io = StringIO(res.text)
            if fname:
                with open(fname, 'wt') as fh:
                    fh.write(res.text)
        data_iter = read_unicode_csv_fileobj(csv_io, delimiter=delimiter, skiprows=1)
    else:
        raise Exception('Could not download Signor data.')
    return data_iter


def _processor_from_data(data_iter, complexes_iter):
    data = [_SignorRow_(*[f.strip() for f in r]) for r in data_iter]
    complex_map = {}
    if complexes_iter:
        for crow in complexes_iter:
            complex_map[crow[0]] = [c for c in crow[2].split(', ') if c]

def process_from_web(signor_data_file=None, signor_complexes_file=None):
    """Process Signor interaction data from the web.

    This downloads the latest interaction data directly from the Signor
    website without an intermediate local file.

    Parameters
    ----------
    signor_data_file : Optional[str]
        If specified, the interaction data will be written to this file.
    signor_complexes_file : Optional[str]
        If specified, the complex data will be written to this file.

    Returns
    -------
    indra.sources.signor.SignorProcessor
        SignorProcessor containing Statements extracted from the Signor data.
    """
    # Get interaction data
    data_url = 'https://signor.uniroma2.it/download_entity.php'
    res = requests.post(data_url, data={'organism': 'human', 'format': 'csv',
                                        'submit': 'Download'})
    data_iter = _handle_response(res, '\t', fname=signor_data_file)
    # Get complexes
    complexes_url = 'https://signor.uniroma2.it/download_complexes.php'
    res = requests.post(complexes_url,
                        data={'submit': 'Download complex data'})
    complexes_iter = _handle_response(res, ';', fname=signor_complexes_file)

```
