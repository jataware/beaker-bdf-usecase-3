# Description
Testing ID lookup with a DOI without prefix and without specifying ID type.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
import pytest
from indra.literature import pmc_client
from indra.util import unicode_strs

example_ids = {'pmid': '25361007',
               'pmcid': 'PMC4322985',

@pytest.mark.webservice
def test_id_lookup_doi_no_prefix_no_idtype():
    ids = pmc_client.id_lookup('10.18632/oncotarget.2555')
    assert ids['doi'] == example_ids['doi']
    assert ids['pmid'] == example_ids['pmid']
    assert ids['pmcid'] == example_ids['pmcid']

```
