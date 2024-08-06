# Description
Testing a complex with unique IDs for generating a model using KamiAssembler.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
import json
from builtins import dict, str
from indra.statements import *
from indra.assemblers.kami import KamiAssembler

egf = Agent('EGF')

def test_unique_id():
    egf = Agent('EGF')
    egfr = Agent('EGFR', bound_conditions=BoundCondition(egf, True))
    stmt = Complex([egfr, egfr])
    ka = KamiAssembler()
    ka.add_statements([stmt])
    model = ka.make_model()

```
