# Description
Filter paragraphs based on whether they contain any of the specified substrings ('NP' or 'NPs').

# Code
```
import logging
import unittest
import pytest
from indra.literature.adeft_tools import universal_extract_paragraphs, filter_paragraphs
from indra.literature import pmc_client, elsevier_client, pubmed_client


def test_universal_extract_texts_contains_union():
    example = ['eeeeeeeeeeNPeeeeeeeeeeeeee',
               'eeeeeee-NPs-eeeeeeeeeeeeee',
               'eeeeeee NP eeeeeeeeeeeeeee',
               'eeeeeeeNPseeeee NP-eeeeeee',
               'eeeeeeeeeeeeeeeeeeeeeeeeee']
    result = ('eeeeeee-NPs-eeeeeeeeeeeeee\n'
              'eeeeeee NP eeeeeeeeeeeeeee\n'
              'eeeeeeeNPseeeee NP-eeeeeee\n')
    text = filter_paragraphs(example, contains=['NP', 'NPs'])

```
