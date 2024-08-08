# Description
Test the ability of the processor to extract which sentence in particular lead to the creation of the INDRA statement, amongst a corpus of text not related to the statement's mechanism.

# Code
```
import pytest
from indra.statements import *
from indra.sources.tees import api

@pytest.mark.slow
def test_evidence_text():
    # Test the ability of the processor to extract which sentence in particular
    # lead to the creation of the INDRA statement, amongst a corpus of text
    # not related to the statement's mechanism.

    # Corpus containing exactly one biological mechanism
    corpus = """Why did the cows return to the marijuana field? It was the pot
    calling the cattle back. Why do cows have hooves instead of feet? Because
    they lactose. When making non-dairy butter, there is little margarine for
    error. Ras leads to the phosphorylation of Raf. Do ghost cows say "moo" or
    "boo"? The surprising fact is they say "moo", but with a rising vibrato
    tone instead of an elongated one."""

    # Process the corpus
    tp = api.process_text(corpus)
    statements = tp.statements

    # Only one of the sentences was related to a biological mechanism
    assert len(statements) == 1
    statement0 = statements[0]

    # Make sure it got the right sentence
    text = statement0.evidence[0].text
    print('Statement text:"', text + '"')

```
