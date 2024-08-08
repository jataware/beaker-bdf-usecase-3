# Description
Test the assembly of an agent string for an agent with multiple modifications.

# Code
```
import indra.assemblers.english.assembler as ea

def test_agent_mods():
    mc1 = ModCondition('phosphorylation', 'tyrosine', '1111')
    mc2 = ModCondition('phosphorylation', 'tyrosine', '1234')
    a = Agent('EGFR', mods=[mc1, mc2])
    ag = ea._assemble_agent_str(a)
    print(ag.agent_str)
    assert ag.agent_str == 'EGFR phosphorylated on Y1111 and Y1234'

```
