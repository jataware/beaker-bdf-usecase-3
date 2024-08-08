# Description
Test getting license links for a DOI

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from indra.literature import crossref_client
from indra.util import unicode_strs
import pytest

@pytest.mark.webservice
def test_get_license_links():
    links = crossref_client.get_license_links(test_doi)
    assert links[0] == 'https://www.elsevier.com/tdm/userlicense/1.0/'
    assert unicode_strs(links)
    links = crossref_client.get_license_links('xyz')

```
