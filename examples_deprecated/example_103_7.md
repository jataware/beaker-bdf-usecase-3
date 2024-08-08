# Description
Require active forms with specific modifications using MechLinker.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.statements import *

def test_require_active_forms_mod1():
    af = ActiveForm(Agent('a', mods=[ModCondition('phosphorylation')]),
                    'activity', True)
    ph = Phosphorylation(Agent('a'), Agent('b'))
    ml = MechLinker([af, ph])
    ml.gather_explicit_activities()
    ml.require_active_forms()
    assert len(ml.statements) == 2

```
