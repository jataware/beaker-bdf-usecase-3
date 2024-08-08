# Description
Create a method to map concepts to biomedical agents by grounding to external ontologies, using optional grounding.

# Code
```
from typing import Any, Callable, Mapping, Optional

from indra.statements import Agent
from indra.ontology.standardize import standardize_agent_name

GrounderResult = Mapping[str, str]

def get_agent_bio(concept, context=None, grounder: Optional[Grounder] = None):
    if not grounder:
        grounder = default_grounder_wrapper
    # Note that currently concept.name is the canonicalized entity text
    # whereas db_refs['TEXT'] is the unaltered original entity text
    raw_txt = concept.db_refs['TEXT']
    norm_txt = concept.name
    # We ground first the raw entity text and if that cannot be grounded,
    # the normalized entity text. The agent name is chosen based on the
    # first text that was successfully grounded, or if no grounding was
    # obtained, is chosen as the normalized text
    for txt in (raw_txt, norm_txt):
        gr = grounder(txt, context=context)
        if gr:
            name = txt
            break
    else:
        gr = {}
        name = norm_txt
    # We take whatever grounding and name are available and then
    # standardize the agent.
    agent = Agent(name, db_refs={'TEXT_NORM': norm_txt,
                                 'TEXT': raw_txt, **gr})
    standardize_agent_name(agent, standardize_refs=True)

```
