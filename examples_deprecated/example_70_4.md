# Description
Test getting full text links for a DOI

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from indra.literature import crossref_client
from indra.util import unicode_strs
import pytest

@pytest.mark.webservice
def test_get_fulltext_links():
    links = crossref_client.get_fulltext_links(test_doi)
    content_types = [l.get('content-type') for l in links]
    assert 'text/plain' in content_types
    assert 'text/xml' in content_types
    assert unicode_strs(links)
    links = crossref_client.get_fulltext_links('xyz')

```
