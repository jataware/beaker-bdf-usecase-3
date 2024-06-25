# Description
Dumping statements into a pickle file and verifying them.

# Code
```
from indra.tools import assemble_corpus as ac
from indra.statements import *

# Assuming these statements have been defined earlier in the script
# Example of an Inhibition statement:

def test_dump_stmts():
    ac.dump_statements([st1], '_test.pkl')
    st_loaded = ac.load_statements('_test.pkl')
    assert len(st_loaded) == 1

```
