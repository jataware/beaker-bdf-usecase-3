# Description
Test case to retrieve drug target data and assert that the list length is greater than 100.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
import unittest
import pytest
from indra.databases.lincs_client import get_drug_target_data, LincsClient


@pytest.mark.webservice
@unittest.skip('LINCS web service very unreliable.')
def test_get_drug_target_data():
    data_list = get_drug_target_data()

```
