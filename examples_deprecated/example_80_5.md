# Description
Test for retrieving an article's text where the expected result is no text (article body is None).

# Code
```
import logging
from indra.literature import elsevier_client as ec
import pytest


@pytest.mark.nonpublic
@pytest.mark.webservice
@pytest.mark.nogha
def test_article():
    # PMID: 11302724
    doi = '10.1006/bbrc.2001.4693'
    xml_str = ec.download_article(doi)
    body = ec.extract_text(xml_str)

```
