# Description
Test the assembly of an agent string for a basic agent without any modifications.

# Code
```
import indra.assemblers.english.assembler as ea

def test_agent_basic():
    ag = ea._assemble_agent_str(Agent('EGFR'))
    assert isinstance(ag, ea.AgentWithCoordinates)
    print(ag.agent_str)
    assert ag.agent_str == 'EGFR'

```
