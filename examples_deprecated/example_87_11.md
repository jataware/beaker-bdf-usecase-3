# Description
Example to create and test handling of duplicate complex statements involving multiple agents.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.statements import *

def test_duplicates():
    st = [Complex([Agent('BRAF'), Agent('RAF1'), Agent('YWAH')])]
    st += [Complex([Agent('BRAF'), Agent('RAF1')])]
    ga = GraphAssembler()
    ga.add_statements(st)
    ga.make_model()
    assert len(ga.graph.nodes()) == 3

```
