# Description
Demonstrates how to use INDRA to perform custom preassembly with agent name and statement type matches

# Code
```
indra.statements import Concept, Event
indra.preassembler.custom_preassembly import agent_name_stmt_type_matches

def test_agent_name_custom_preassembly():
    e1 = Event(Concept('price oil'))
    e2 = Event(Concept('oil price'))
    stmts = [e1, e2]
    stmts_out = ac.run_preassembly(stmts,
                                   matches_fun=agent_name_stmt_type_matches)

```
