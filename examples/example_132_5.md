# Description
Test example demonstrating how to use the `fix_agent` function to correct the name and database references of an `Agent` instance with another set of NCIT references.

# Code
```
import json
from indra.sources import sparser
from indra.sources.sparser.processor import fix_agent

def test_fix_agent_ncit_only():
    a = Agent('XXX', db_refs={'NCIT': 'C129655'})
    fix_agent(a)
    assert a.name == 'TUBB'

```
