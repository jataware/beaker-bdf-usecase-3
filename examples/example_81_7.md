# Description
Test the assembly of an agent string for an agent with an activation condition.

# Code
```
import indra.assemblers.english.assembler as ea

def test_agent_activity():
    a = Agent('BRAF', activity=ActivityCondition('activity', True))
    ag = ea._assemble_agent_str(a)
    print(ag.agent_str)
    assert ag.agent_str == 'active BRAF'

```
