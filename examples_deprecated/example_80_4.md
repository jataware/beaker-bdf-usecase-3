# Description
Test for retrieving the content of an article with `xocs:rawtext` in its XML structure. Ensures the extraction of raw text.

# Code
```
import logging
from indra.literature import elsevier_client as ec
import pytest


@pytest.mark.nonpublic
@pytest.mark.webservice
@pytest.mark.nogha
def test_get_rawtext():
    """Make sure we can get content of an article that has content in
    xocs:rawtext"""
    # PMID: 20072652
    doi = '10.1593/neo.91196'
    xml_str = ec.download_article(doi)
    body = ec.extract_text(xml_str)
    if not body:
        logger.warning('Unable to extract text from XML string:\n'
                       '%s...' % xml_str[:2000])

```
