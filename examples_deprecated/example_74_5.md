# Description
Test complex formation statements using CyJSAssembler.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from indra.statements import *
from indra.assemblers.cyjs import CyJSAssembler
mek = Agent('MAP2K1', db_refs={'HGNC': '6840', 'TEXT': 'mek1'})
erk = Agent('MAPK1', db_refs={'UP': 'P28482'})
dusp = Agent('DUSP4')

def test_complex():
    cja = CyJSAssembler()
    cja.add_statements([st_complex])
    cja.make_model()
    assert len(cja._nodes) == 3
    assert len(cja._edges) == 3
    polarities = [edge['data']['polarity'] for edge in cja._edges]
    assert len(set(polarities))==1

```
