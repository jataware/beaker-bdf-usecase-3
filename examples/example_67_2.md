# Description
This code example shows how to query activity data for a molecule (`vem_chembl_id`) using the `send_query` function from the `chembl_client` module and then verifies the results and assay types.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from indra.databases import chembl_client
import pytest

vem_chembl_id = 'CHEMBL1229517'

@pytest.mark.webservice
@pytest.mark.nogha
def test_activity_query():
    res = chembl_client.send_query(query_dict_vem_activity)
    assert res['page_meta']['total_count'] == len(res['activities'])
    assay_types = list(set([x['standard_type'] for x in res['activities']]))
    expected_types = ['IC50', 'EC50', 'INH', 'Potency']
    for e_t in expected_types:

```
