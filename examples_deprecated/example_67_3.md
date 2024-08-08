# Description
This code example shows how to query target data for a target (`braf_chembl_id`) using the `query_target` function from the `chembl_client` module and verifies the target type.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from indra.databases import chembl_client
import pytest


@pytest.mark.webservice
def test_target_query():
    target = chembl_client.query_target(braf_chembl_id)

```
