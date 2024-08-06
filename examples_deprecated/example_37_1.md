# Description
Register and implement a function to get an Agent matches key based on grounding.

# Code
```
import logging
from indra.statements import *
from indra.pipeline import register_pipeline

@register_pipeline
def agent_grounding_matches(agent):
    """Return an Agent matches key just based on grounding, not state."""
    if agent is None:
        return None

```
