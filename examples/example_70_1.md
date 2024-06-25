# Description
Test querying DOI using a PMID

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from indra.literature import crossref_client
from indra.util import unicode_strs
import pytest

@pytest.mark.webservice
def test_doi_query():
    mapped_doi = crossref_client.doi_query(example_ids['pmid'])
    assert mapped_doi == example_ids['doi']

```
