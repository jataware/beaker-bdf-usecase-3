# Description
Test case to fetch small molecule references for given IDs and validate the results.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
import unittest
import pytest
from indra.databases.lincs_client import get_drug_target_data, LincsClient


def test_get_sm_refs():
    sm_refs = lc.get_small_molecule_refs('10001')
    assert sm_refs.get('HMS-LINCS') == '10001', sm_refs
    assert sm_refs.get('PUBCHEM') == '160355', sm_refs
    assert sm_refs.get('CHEMBL') == 'CHEMBL14762', sm_refs

    sm_refs = lc.get_small_molecule_refs('10001-101')
    assert sm_refs.get('HMS-LINCS') == '10001-101', sm_refs

```
