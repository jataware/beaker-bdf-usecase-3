# Description
Filtering statements to include only those grounded to known entities and exceeding a score threshold.

# Code
```
from indra.tools import assemble_corpus as ac
from indra.statements import *

# Example Influence statements
c1 = Event(Concept('x', db_refs={'a': [('x', 0.5), ('y', 0.8)]}))

def test_filter_grounded_only_score():
    c1 = Event(Concept('x', db_refs={'a': [('x', 0.5), ('y', 0.8)]}))
    c2 = Event(Concept('x', db_refs={'a': [('x', 0.7), ('y', 0.9)]}))
    st1 = Influence(c1, c2)
    assert len(ac.filter_grounded_only([st1])) == 1
    assert len(ac.filter_grounded_only([st1], score_threshold=0.4)) == 1
    assert len(ac.filter_grounded_only([st1], score_threshold=0.6)) == 1
    assert len(ac.filter_grounded_only([st1], score_threshold=0.85)) == 0

```
