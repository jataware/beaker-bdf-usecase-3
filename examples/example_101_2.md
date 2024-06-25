# Description
Test case to fetch protein references for a given protein ID and validates the results.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
import unittest
import pytest
from indra.databases.lincs_client import get_drug_target_data, LincsClient


def test_get_protein_refs():
    prot_refs = lc.get_protein_refs('200020')
    assert prot_refs.get('UP') == 'P00519'
    assert prot_refs.get('EGID') == '25'

```
