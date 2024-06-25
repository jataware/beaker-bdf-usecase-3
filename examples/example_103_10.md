# Description
Replace activation statements using MechLinker.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.statements import *

def test_replace_activations():
    af = ActiveForm(Agent('a', mods=[ModCondition('phosphorylation')]),
                    'activity', True)
    phos = Phosphorylation(Agent('b'), Agent('a'))
    act = Activation(Agent('b'), Agent('a'))
    ml = MechLinker([af, phos, act])
    ml.replace_activations()
    assert len(ml.statements) == 2

```
