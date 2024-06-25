# Description
Test example demonstrating how to use the `fix_agent` function to correct the name and database references of an `Agent` instance with HGNC (HUGO Gene Nomenclature Committee) references.

# Code
```
import json
from indra.sources import sparser
from indra.sources.sparser.processor import fix_agent

def test_fix_agent_hgnc_only():
    a = Agent('XXX', db_refs={'HGNC': '7199'})
    fix_agent(a)
    assert a.name == 'MOS'

```
