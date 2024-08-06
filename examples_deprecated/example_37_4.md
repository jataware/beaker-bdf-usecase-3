# Description
Register and implement a function to get a matches key based on normalized Agent name and Statement type.

# Code
```
import logging
from indra.statements import *
from indra.pipeline import register_pipeline
logger = logging.getLogger(__name__)
@register_pipeline
def agent_name_matches(agent):
    if agent is None:
        return None
    bw = '_'.join(sorted(list(set(agent.name.lower().split()))))

@register_pipeline
def agent_name_stmt_type_matches(stmt):
    """Return True if the statement type and normalized agent name matches."""
    agents = [agent_name_matches(a) for a in stmt.agent_list()]
    key = str((stmt.__class__.__name__, agents))

```
