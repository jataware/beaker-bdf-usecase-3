# Description
Test case to fetch a small molecule name for a given ID and validate the returned name.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
import unittest
import pytest
from indra.databases.lincs_client import get_drug_target_data, LincsClient


def test_get_sm_name():
    sm_name = lc.get_small_molecule_name('10001')

```
