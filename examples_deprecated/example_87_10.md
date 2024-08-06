# Description
Example to create and test an association statement involving events and concepts.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.statements import *

def test_association():
    st = [Association([Event(Concept('a')), Event(Concept('b'))])]
    ga = GraphAssembler()
    ga.add_statements(st)
    ga.make_model()
    assert len(ga.graph.nodes()) == 2

```
