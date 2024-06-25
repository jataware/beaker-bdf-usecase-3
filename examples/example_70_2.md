# Description
Test getting metadata for a DOI

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from indra.literature import crossref_client
from indra.util import unicode_strs
import pytest

@pytest.mark.webservice
def test_get_metadata():
    metadata = crossref_client.get_metadata(test_doi)
    assert metadata['DOI'] == test_doi
    assert unicode_strs(metadata)
    metadata = crossref_client.get_metadata('xyz')

```
