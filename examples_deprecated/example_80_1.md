# Description
Test for retrieving the full text of an article using its DOI. This test checks whether the article is accessible through the API.

# Code
```
import logging
from indra.literature import elsevier_client as ec
import pytest


@pytest.mark.nonpublic
@pytest.mark.webservice
@pytest.mark.nogha
def test_get_fulltext_article():
    # This article is not open access so in order to get a full text response
    # with a body element requires full text access keys to be correctly
    # set up.
    doi = '10.1016/j.cell.2016.02.059'
    text = ec.get_article(doi)

```
