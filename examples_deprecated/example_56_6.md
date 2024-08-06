# Description
Filtering statements to include only those where the agents are human genes.

# Code
```
from indra.tools import assemble_corpus as ac
from indra.statements import *

# Assuming these statements have been defined earlier in the script:
st1 = Phosphorylation(Agent('a', db_refs={'HGNC': '1234', 'TEXT': 'a'}), Agent('b', db_refs={'UP': 'P15056', 'TEXT': 'b'}), evidence=[Evidence(text='a->b', source_api='assertion')])
st5 = Phosphorylation(None, Agent('b', db_refs={'UP': 'P15056', 'TEXT': 'b'}), evidence=[Evidence(text='->b', source_api='assertion')])
st6 = Phosphorylation(None, Agent('d', db_refs={'TEXT': 'd'}), evidence=[Evidence(text='->d', source_api='assertion')])

def test_filter_genes_only():
    st_out = ac.filter_genes_only([st1, st5])
    assert len(st_out) == 2
    st_out = ac.filter_genes_only([st6, st7])
    assert len(st_out) == 0
    st_out = ac.filter_genes_only([st4])
    assert len(st_out) == 0
    st_out = ac.filter_genes_only([st3], specific_only=True)
    assert len(st_out) == 0

    # Can we remove statements with non-gene bound conditions?
    st_out = ac.filter_genes_only([st18])  # remove_bound defaults to False
    assert len(st_out) == 0
    st_out = ac.filter_genes_only([st18], remove_bound=False)
    assert len(st_out) == 0

    # Can we remove non-gene bound conditions?
    st18_copy = deepcopy(st18)
    assert len(st18_copy.sub.bound_conditions) == 1
    st_out = ac.filter_genes_only([st18_copy], remove_bound=True)

```
