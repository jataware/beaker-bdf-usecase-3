# Description
Test example demonstrating how to use the `fix_agent` function to correct the name and database references of an `Agent` instance with FA (functional annotation) references.

# Code
```
import json
from indra.sources import sparser
from indra.sources.sparser.processor import fix_agent

def test_fix_agent_fa_only():
    a = Agent('XXX', db_refs={'FA': '00815'})
    fix_agent(a)
    assert a.name == 'Cyclin'
    assert a.db_refs.get('FPLX') == 'Cyclin'
    assert a.db_refs.get('NXPFA') == '00815'

```
