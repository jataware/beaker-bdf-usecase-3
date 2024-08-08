# Description
Filtering statements by a specific UUID list.

# Code
```
from indra.tools import assemble_corpus as ac
from indra.statements import *

# Assuming these statements have been defined earlier in the script
# Example Phosphorylation statement:
st1 = Phosphorylation(Agent('a', db_refs={'HGNC': '1234', 'TEXT': 'a'}), Agent('b', db_refs={'UP': 'P15056', 'TEXT': 'b'}), evidence=[Evidence(text='a->b', source_api='assertion')])

def test_filter_uuid_list():
    st_out = ac.filter_uuid_list([st1, st4], [st1.uuid])

```
