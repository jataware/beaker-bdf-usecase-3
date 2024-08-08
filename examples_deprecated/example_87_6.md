# Description
Example to create and test an inhibition statement involving two agents.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.statements import *

def test_inactivation():
    st = [Inhibition(Agent('DUSP4'), Agent('MAPK1'))]
    ga = GraphAssembler()
    ga.add_statements(st)
    ga.make_model()
    assert len(ga.graph.nodes()) == 2

```