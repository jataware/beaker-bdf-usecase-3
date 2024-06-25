# Description
Create and assert properties of an AgentState.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.statements import *

def test_agent_state():
    mc = ModCondition('phosphorylation')
    mut = MutCondition('600', 'V', 'E')
    location = 'nucleus'
    bc = BoundCondition(Agent('x'), True)
    a = Agent('a', mods=[mc], mutations=[mut], bound_conditions=[bc],
              location=location)
    agent_state = AgentState(a)
    assert agent_state.mods
    assert agent_state.mutations
    assert agent_state.bound_conditions

```
