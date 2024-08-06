# Description
Infer modifications from activation and active form statements using MechLinker.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.statements import *

def test_act_af_to_phos():
    act_st = Activation(Agent('A', activity=ActivityCondition('kinase', True)),
                        Agent('B'))
    af_st = ActiveForm(Agent('B', mods=[ModCondition('phosphorylation',
                                                     None, None, True)]),
                        'activity', True)
    ml = MechLinker([act_st, af_st])
    linked_stmts = ml.infer_modifications(ml.statements)

```
