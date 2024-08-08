# Description
Reduce activity types using MechLinker.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.statements import *

def test_reduce_activity_types():
    a1 = Agent('a', location='cytoplasm')
    a2 = Agent('a', location='nucleus')
    af1 = ActiveForm(a1, 'activity', True)
    af2 = ActiveForm(a2, 'kinase', True)
    af3 = ActiveForm(a1, 'catalytic',True)
    ml = MechLinker([af1, af2, af3])
    ml.gather_explicit_activities()
    ml.reduce_activities()
    assert af1.activity == 'kinase'
    assert af2.activity == 'kinase'

```
