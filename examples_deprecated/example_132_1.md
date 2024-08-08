# Description
Test example demonstrating how to use the `fix_agent` function to correct the name and database references of an `Agent` instance with FPLX (famplex) references.

# Code
```
import json
from indra.sources import sparser
from indra.sources.sparser.processor import fix_agent

def test_fix_agent_be_name():
    a = Agent('XXX', db_refs={'FPLX': 'CDK'})
    fix_agent(a)

```
