# Description
Infer complexes from phosphorylation statements using MechLinker.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.statements import *

def test_infer_complexes():
    phos = Phosphorylation(Agent('b'), Agent('a'))
    linked_stmts = MechLinker.infer_complexes([phos])
    assert len(linked_stmts) == 1

```
