# Description
Require active forms with specific locations using MechLinker.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.statements import *

def test_require_active_forms_mod2():
    af = ActiveForm(Agent('a', mods=[ModCondition('phosphorylation')]),
                    'activity', True)
    af2 = ActiveForm(Agent('a', location='nucleus'), 'activity', True)
    ph = Phosphorylation(Agent('a'), Agent('b'))
    ml = MechLinker([af, af2, ph])
    ml.gather_explicit_activities()
    ml.require_active_forms()
    assert len(ml.statements) == 4

```
