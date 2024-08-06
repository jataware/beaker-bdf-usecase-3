# Description
Example to create and test a phosphorylation statement involving two agents.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.statements import *

def test_phosphorylation():
    st = [Phosphorylation(Agent('MAP2K1'), Agent('MAPK1'))]
    ga = GraphAssembler()
    ga.add_statements(st)
    model = ga.make_model()
    assert 'MAP2K1' in model
    assert len(ga.graph.nodes()) == 2

```
