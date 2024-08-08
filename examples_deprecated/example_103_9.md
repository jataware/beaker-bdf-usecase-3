# Description
Infer activations based on post-translational modifications using MechLinker.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.statements import *

def test_infer_activations():
    af = ActiveForm(Agent('a', mods=[ModCondition('phosphorylation')]),
                    'activity', True)
    phos = Phosphorylation(Agent('b'), Agent('a'))
    linked_stmts = MechLinker.infer_activations([af, phos])
    assert len(linked_stmts) == 1

```
