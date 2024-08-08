# Description
Test RAS-related statements using CyJSAssembler.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from indra.statements import *
from indra.assemblers.cyjs import CyJSAssembler
st_gef = Gef(Agent('SOS1'), Agent('HRAS'))

def test_ras():
    cja = CyJSAssembler()
    cja.add_statements([st_gef, st_gap])
    cja.make_model()
    assert len(cja._nodes) == 3
    assert len(cja._edges) == 2
    polarities = [edge['data']['polarity'] for edge in cja._edges]
    assert len(set(polarities))==2
    assert 'positive' in polarities

```
