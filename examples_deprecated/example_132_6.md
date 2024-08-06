# Description
Test example demonstrating how to use the `fix_agent` function to correct the database references of an `Agent` instance with PCID (PubChem Compound ID) references.

# Code
```
import json
from indra.sources import sparser
from indra.sources.sparser.processor import fix_agent

def test_fix_agent_pcid():
    a = Agent('XXX', db_refs={'PCID': '123'})
    fix_agent(a)
    assert 'PCID' not in a.db_refs

```
