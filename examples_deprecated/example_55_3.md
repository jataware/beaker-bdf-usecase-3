# Description
Test the extraction of an abstract from a PubMed article using its PMID.

# Code
```
import logging
import unittest
import pytest
from indra.literature.adeft_tools import universal_extract_paragraphs, filter_paragraphs
from indra.literature import pmc_client, elsevier_client, pubmed_client


@pytest.mark.webservice
def test_universal_extract_paragraphs_abstract():
    pmid = '16511588'
    abstract = pubmed_client.get_abstract(pmid)
    result = universal_extract_paragraphs(abstract)

```
