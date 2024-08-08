# Description
Replace complex statements using MechLinker.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.statements import *

def test_replace_complexes():
    phos = Phosphorylation(Agent('b'), Agent('a'))
    cplx = Complex([Agent('a'), Agent('b')])
    ml = MechLinker([phos, cplx])
    ml.replace_complexes()
    assert len(ml.statements) == 1

```
