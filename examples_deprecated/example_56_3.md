# Description
Filtering statements to include only those grounded to known entities.

# Code
```
from copy import deepcopy
from indra.tools import assemble_corpus as ac
from indra.statements import *

# Assuming these statements have been defined earlier in the script
# Example Phosphorylation statements:
st18 = Phosphorylation(Agent('a'), Agent('i', db_refs={'HGNC': '1234', 'TEXT': 'a'}, bound_conditions=[BoundCondition(Agent('d', db_refs={'TEXT': 'd'}))]))
st4 = Phosphorylation(Agent('b'), Agent('e', db_refs={'CHEBI': 'CHEBI:1234', 'TEXT': 'e'}), evidence=[Evidence(text='b->e', source_api='assertion')])
st1 = Phosphorylation(Agent('a'), Agent('b', db_refs={'UP': 'P15056', 'TEXT': 'b'}), evidence=[Evidence(text='a->b', source_api='assertion')])

def test_filter_grounded_only():
    # st18 has and i, which has an ungrounded bound condition
    st_out = ac.filter_grounded_only([st1, st4])
    assert len(st_out) == 2
    st_out = ac.filter_grounded_only([st3])
    assert len(st_out) == 0

    # Do we filter out a statement with an ungrounded bound condition?
    st_out = ac.filter_grounded_only([st18])
    assert len(st_out) == 0

    # When we request to remove ungrounded bound conditions, do we?
    st18_copy = deepcopy(st18)
    assert len(st18_copy.sub.bound_conditions) == 1
    st_out = ac.filter_grounded_only([st18_copy], remove_bound=True)
    assert len(st_out[0].sub.bound_conditions) == 0

    # When we request to remove ungrounded bound conditions, do we leave
    # grounded bound conditions in place?
    st19_copy = deepcopy(st19)
    assert len(st19_copy.sub.bound_conditions) == 1
    st_out = ac.filter_grounded_only([st19_copy], remove_bound=True)
    assert len(st_out[0].sub.bound_conditions) == 1

    # Do we filter out a statement with an grounded bound condition?
    st_out = ac.filter_grounded_only([st19])

```
