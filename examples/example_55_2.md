# Description
Test the extraction of paragraphs from a PMC article using its PMC ID.

# Code
```
import logging
import unittest
import pytest
from indra.literature.adeft_tools import universal_extract_paragraphs, filter_paragraphs
from indra.literature import pmc_client, elsevier_client, pubmed_client


@pytest.mark.webservice
def test_universal_extract_paragraphs_pmc():
    pmc_id = 'PMC3262597'
    xml_str = pmc_client.get_xml(pmc_id)
    paragraphs = universal_extract_paragraphs(xml_str)

```
