# Description
Check the initialization of node agents in the processed CX file

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
import os
from indra.sources.ndex_cx import process_cx_file
from indra.sources.ndex_cx.processor import NdexCxProcessor
from indra.statements import Agent
path_this = os.path.dirname(os.path.abspath(__file__))

def test_initialize_node_agents():
    assert isinstance(ncp_file._node_agents, dict)
    for ndex_id, agent in ncp_file._node_agents.items():
        assert isinstance(ndex_id, int)
        assert isinstance(agent, Agent)
        assert agent.db_refs.get('HGNC')

```
