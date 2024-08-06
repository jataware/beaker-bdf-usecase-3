# Description
Filter paragraphs based on whether they contain a specific substring ('ER').

# Code
```
import logging
import unittest
import pytest
from indra.literature.adeft_tools import universal_extract_paragraphs, filter_paragraphs
from indra.literature import pmc_client, elsevier_client, pubmed_client


def test_universal_extract_texts_contains():
    example = ['eeeeeeeeeeeeeEReeeeeeeeee',
               'eeeeeee-ER-eeeeeeeeeeeeee',
               'eeeeeee ER eeeeeeeeeeeeee',
               'eeeeeeeER eeeeeeeeeeeeeee']
    result = ('eeeeeee-ER-eeeeeeeeeeeeee\n'
              'eeeeeee ER eeeeeeeeeeeeee\n')
    text = filter_paragraphs(example, contains='ER')

```
