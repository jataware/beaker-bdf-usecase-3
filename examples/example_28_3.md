# Description
Extract paragraphs from XML that could be from different sources (e.g., Elsevier or NLM).

# Code
```
import logging
from indra.literature import pubmed_client, pmc_client, elsevier_client

logger = logging.getLogger(__name__)

# the elsevier_client will log messages that it is safe to ignore
el = logging.getLogger('indra.literature.elsevier_client')

def universal_extract_paragraphs(xml):
    """Extract paragraphs from xml that could be from  different sources

    First try to parse the xml as if it came from elsevier. if we do not
    have valid elsevier xml this will throw an exception. the text extraction
    function in the pmc client may not throw an exception when parsing elsevier
    xml, silently processing the xml incorrectly

    Parameters
    ----------
    xml : str
       Either an NLM xml, Elsevier xml or plaintext

    Returns
    -------
    paragraphs : str
        Extracted plaintext paragraphs from NLM or Elsevier XML
    """
    try:
        paragraphs = elsevier_client.extract_paragraphs(xml)
    except Exception:
        paragraphs = None
    if paragraphs is None:
        try:
            paragraphs = pmc_client.extract_paragraphs(xml)
        except Exception:
            paragraphs = [xml]

```
