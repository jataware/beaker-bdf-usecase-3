# Description
Test getting publisher information for a DOI

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from indra.literature import crossref_client
from indra.util import unicode_strs
import pytest

@pytest.mark.webservice
def test_get_publisher():
    publisher = crossref_client.get_publisher(test_doi)
    assert publisher == 'Elsevier BV'
    assert unicode_strs(publisher)
    publisher = crossref_client.get_publisher('xyz')

```
