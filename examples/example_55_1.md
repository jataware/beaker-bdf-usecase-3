# Description
Test the extraction of paragraphs from an Elsevier article using its DOI.

# Code
```
import logging
import unittest
import pytest
from indra.literature.adeft_tools import universal_extract_paragraphs, filter_paragraphs
from indra.literature import pmc_client, elsevier_client, pubmed_client


@pytest.mark.nonpublic
@pytest.mark.webservice
@unittest.skip('Elsevier credentials currently not operational')
def test_universal_extract_paragraphs_elsevier():
    doi = '10.1016/B978-0-12-416673-8.00004-6'
    xml_str = elsevier_client.download_article(doi)
    paragraphs = universal_extract_paragraphs(xml_str)
    if len(paragraphs) <= 1:
        logger.warning('Unable to extract paragraphs from XML string:\n'
                       '%s...' % xml_str[:2000])

```
