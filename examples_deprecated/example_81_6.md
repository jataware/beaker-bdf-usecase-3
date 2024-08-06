# Description
Test the assembly of an agent string for an agent bound to another agent.

# Code
```
import indra.assemblers.english.assembler as ea

def test_agent_bound():
    bc = BoundCondition(Agent('EGF'), True)
    a = Agent('EGFR', bound_conditions=[bc])
    ag = ea._assemble_agent_str(a)
    print(ag.agent_str)
    assert ag.agent_str == 'EGFR bound to EGF'

```
