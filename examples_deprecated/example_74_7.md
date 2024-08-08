# Description
Test no grouping in CyJSAssembler model.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.statements import *

def test_no_grouping():
    st1 = Phosphorylation(Agent('A'), Agent('B'))
    st2 = Phosphorylation(Agent('A'), Agent('C'))
    st3 = Phosphorylation(Agent('C'), Agent('B'))
    cja = CyJSAssembler()
    cja.add_statements([st1, st2, st3])
    cja.make_model(grouping=True)
    parents = [node['data']['parent'] for node in cja._nodes]
    for parent in parents:

```
