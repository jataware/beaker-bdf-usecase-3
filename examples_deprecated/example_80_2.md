# Description
Test for retrieving the abstract of an article using its DOI, ensuring that the API key is functioning even if full access is not available.

# Code
```
import logging
from indra.literature import elsevier_client as ec
import pytest


@pytest.mark.nonpublic
@pytest.mark.webservice
@pytest.mark.nogha
def test_get_abstract():
    # If we have an API key but are not on an approved IP or don't have a
    # necessary institution key, we should still be able to get the abstract.
    # If there is a problem with the API key itself, this will log and error
    # and return None.
    doi = '10.1016/j.cell.2016.02.059'
    text = ec.get_abstract(doi)

```
