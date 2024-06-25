# Description
Register and implement a function to get a normalized bag of words from an Agent's name.

# Code
```
import logging
from indra.statements import *
from indra.pipeline import register_pipeline

@register_pipeline
def agent_name_matches(agent):
    """Return a sorted, normalized bag of words as the name."""
    if agent is None:
        return None
    bw = '_'.join(sorted(list(set(agent.name.lower().split()))))

```
