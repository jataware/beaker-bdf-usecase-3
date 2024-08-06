# Description
Example to create and test a dephosphorylation statement without an enzyme.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.statements import *

def test_dephosphorylation_noenz():
    st = [Dephosphorylation(None, Agent('MAPK1'))]
    ga = GraphAssembler()
    ga.add_statements(st)
    ga.make_model()
    assert len(ga.graph.nodes()) == 0

```
