# Description
Retrieve statements from the processed CX file and validate them

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
import os
from indra.sources.ndex_cx import process_cx_file
from indra.sources.ndex_cx.processor import NdexCxProcessor
from indra.statements import Agent, Statement
path_this = os.path.dirname(os.path.abspath(__file__))

def test_get_statements():
    stmts = ncp_file.get_statements()
    for stmt in stmts:
        assert isinstance(stmt, Statement)
        for ag in stmt.agent_list():
            assert isinstance(ag, Agent)
        for ev in stmt.evidence:

```
