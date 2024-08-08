# Description
Testing the processing of SIGNOR data fetched from the web.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str

from os.path import join, dirname
import pytest

from indra.statements import *
from indra.databases import hgnc_client
from indra.sources.signor.processor import SignorProcessor, _parse_residue_positions

@pytest.mark.webservice
@pytest.mark.slow
def test_parse_csv_from_web():
    sp = process_from_web()
    assert isinstance(sp._data, list)
    assert isinstance(sp._data[0], _SignorRow_)
    assert isinstance(sp.statements, list)
    assert isinstance(sp.statements[0], Statement)
    # Test the complex map
    assert isinstance(sp.complex_map, dict)
    assert 'SIGNOR-C1' in sp.complex_map
    assert isinstance(sp.complex_map['SIGNOR-C1'], list)
    assert set(sp.complex_map['SIGNOR-C1']) == {'P23511', 'P25208', 'Q13952'}
    # Make sure we don't error if Complexes data is not provided
    for stmt in sp.statements:
        if isinstance(stmt, Complex):
            if len(stmt.members) < 2:
                assert False, 'Found a complex with less than 2 members: %s' %\

```
