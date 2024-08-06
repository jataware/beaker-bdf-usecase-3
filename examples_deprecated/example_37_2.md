# Description
Register and implement a function to get a matches key based on Agent grounding and Statement type.

# Code
```
import logging
from indra.statements import *
from indra.pipeline import register_pipeline
logger = logging.getLogger(__name__)
@register_pipeline
def agent_grounding_matches(agent):
    if agent is None:
        return None

@register_pipeline
def agents_stmt_type_matches(stmt):
    """Return a matches key just based on Agent grounding and Stmt type."""
    agents = [agent_grounding_matches(a) for a in stmt.agent_list()]
    key = str((stmt.__class__.__name__, agents))

```
