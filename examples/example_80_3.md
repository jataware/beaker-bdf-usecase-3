# Description
Test for retrieving the full text of an article with a specific XML structure `ja:converted-article`. Checks the conversion process from XML to text.

# Code
```
import logging
from indra.literature import elsevier_client as ec
import pytest


@pytest.mark.nonpublic
@pytest.mark.webservice
@pytest.mark.nogha
def test_get_converted_article_body():
    """Make sure we can get fulltext of an article that has
    ja:converted-article as its principal sub-element."""
    # PMID: 11851341
    doi = '10.1006/jmbi.2001.5334'
    xml_str = ec.download_article(doi)
    body = ec.extract_text(xml_str)
    if not body:
        logger.warning('Unable to extract text from XML string:\n'
                       '%s...' % xml_str[:2000])

```
