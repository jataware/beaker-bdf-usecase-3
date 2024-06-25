# Description
Register and implement a function to get normalized Agent names from a Statement.

# Code
```
import logging
from indra.statements import *
from indra.pipeline import register_pipeline

@register_pipeline
def agent_name_stmt_matches(stmt):
    """Return the normalized agent names."""
    agents = [ag.name for ag in stmt.real_agent_list()]
    key = str(agents)

```
