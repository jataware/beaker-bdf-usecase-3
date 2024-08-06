# Description
Testing the processing of SIGNOR data from a local CSV file, including both data files and complexes.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str

from os.path import join, dirname
import pytest

from indra.statements import *
from indra.databases import hgnc_client
from indra.sources.signor.processor import SignorProcessor, _parse_residue_positions
from indra.sources.signor.api import _SignorRow_, process_from_file, process_from_web

test_data_file = join(dirname(__file__), 'signor_test_data.csv')

def test_parse_csv_from_file():
    # Should work with both data file and complexes
    sp = process_from_file(test_data_file, test_complexes_file,
                           delimiter=';')
    assert isinstance(sp._data, list)
    assert isinstance(sp._data[0], _SignorRow_)
    assert isinstance(sp.statements, list)
    assert isinstance(sp.statements[0], Statement)
    # Test the complex map
    assert isinstance(sp.complex_map, dict)
    assert len(sp.complex_map) == 9
    assert 'SIGNOR-C1' in sp.complex_map
    assert isinstance(sp.complex_map['SIGNOR-C1'], list)
    assert sp.complex_map['SIGNOR-C1'] == ['P23511', 'P25208', 'Q13952']
    # Make sure we don't error if Complexes data is not provided
    sp = process_from_file(test_data_file, delimiter=';')
    assert isinstance(sp.statements[0], Statement)

```
