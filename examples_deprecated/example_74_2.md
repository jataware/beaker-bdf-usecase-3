# Description
Test regulation of amount statements using CyJSAssembler.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from indra.statements import *
from indra.assemblers.cyjs import CyJSAssembler
st_incamount = IncreaseAmount(Agent('TP53'), Agent('MDM2'))

def test_regamount():
    cja = CyJSAssembler()
    cja.add_statements([st_incamount, st_decamount])
    cja.make_model()
    assert len(cja._nodes) == 2
    assert len(cja._edges) == 2
    polarities = [edge['data']['polarity'] for edge in cja._edges]
    assert len(set(polarities))==2
    assert 'positive' in polarities

```
