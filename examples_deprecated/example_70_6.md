# Description
Test getting URL for a DOI

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from indra.literature import crossref_client
from indra.util import unicode_strs
import pytest

@pytest.mark.webservice
def test_get_url():
    url = crossref_client.get_url(test_doi)
    assert url == 'http://dx.doi.org/10.1016/j.ccell.2016.02.010'
    assert unicode_strs(url)
    url = crossref_client.get_url('xyz')

```
