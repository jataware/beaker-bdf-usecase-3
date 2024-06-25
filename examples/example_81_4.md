# Description
Test the assembly of an agent string for an agent with a modification specifying the residue and position.

# Code
```
import indra.assemblers.english.assembler as ea

def test_agent_mod3():
    mc = ModCondition('phosphorylation', 'tyrosine', '1111')
    a = Agent('EGFR', mods=mc)
    ag = ea._assemble_agent_str(a)
    print(ag.agent_str)
    assert ag.agent_str == 'EGFR phosphorylated on Y1111'

```
