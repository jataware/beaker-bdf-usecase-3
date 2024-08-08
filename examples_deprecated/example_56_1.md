# Description
Loading statements from a pickle file and verifying them.

# Code
```
import pickle
from indra.tools import assemble_corpus as ac
from indra.statements import *

# Assuming these statements have been defined earlier in the script
# Example of an Inhibition statement:

def test_load_stmts():
    with open('_test.pkl', 'wb') as fh:
        pickle.dump([st1], fh)
    st_loaded = ac.load_statements('_test.pkl')
    assert len(st_loaded) == 1

```
