# Description
Testing retrieval of the title for a given PMCID.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
import pytest

@pytest.mark.webservice
def test_get_title():
    title = pmc_client.get_title('PMC4322985')
    assert title == (
        'BRAF vs RAS oncogenes: are mutations of the same pathway equal? '

```
