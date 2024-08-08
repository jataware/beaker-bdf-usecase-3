# Description
Extract plaintext from XML that could be from different sources, with an option to filter paragraphs based on a list of strings.

# Code
```
import re
import logging
from indra.literature import pubmed_client, pmc_client, elsevier_client

logger = logging.getLogger(__name__)

# the elsevier_client will log messages that it is safe to ignore
el = logging.getLogger('indra.literature.elsevier_client')

def universal_extract_text(xml, contains=None):
    """Extract plaintext from xml that could be from different sources

    Parameters
    ----------
    xml : str
        Either an NLM xml, Elsevier xml, or plaintext

    contains : str or list of str
         Exclude paragraphs not containing this string, or at least one
         of the strings in contains if it is a list

    Returns
    -------
    str
        The concatentation of all paragraphs in the input xml, excluding
        paragraphs not containing one of the tokens in the list contains.
        Paragraphs are separated by new lines.
    """
    paragraphs = universal_extract_paragraphs(xml)

```
