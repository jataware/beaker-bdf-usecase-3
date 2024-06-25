# Description
Register and implement a function to get a key for normalized Agent names and polarity.

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
def agent_name_polarity_matches(stmt, sign_dict):
    """Return a key for normalized agent names and polarity."""
    agents = [ag.name for ag in stmt.real_agent_list()]
    if isinstance(stmt, Influence):
        stmt_pol = stmt.overall_polarity()
        if stmt_pol == 1:
            pol = 0
        elif stmt_pol == -1:
            pol = 1
        else:
            pol = None
    else:
        pol = sign_dict.get(type(stmt).__name__)
    if not pol:
        logger.debug('Unknown polarity for %s' % type(stmt).__name__)
    key = str((agents, pol))

```
