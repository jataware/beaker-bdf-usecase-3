# Description
Test the assembly of an agent string for an agent with a single modification.

# Code
```
import indra.assemblers.english.assembler as ea

def test_agent_mod():
    mc = ModCondition('phosphorylation')
    a = Agent('EGFR', mods=mc)
    ag = ea._assemble_agent_str(a)
    print(ag.agent_str)
    assert ag.agent_str == 'phosphorylated EGFR'

```
