# Description
Example to create and test an influence statement involving events and concepts.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.statements import *

def test_influence():
    # Add an extra standalone event just to make sure it doesn't error
    st = [Influence(Event(Concept('a')), Event(Concept('b'))),
          Event(Concept('a'))]
    ga = GraphAssembler()
    ga.add_statements(st)
    ga.make_model()
    assert len(ga.graph.nodes()) == 2

```
