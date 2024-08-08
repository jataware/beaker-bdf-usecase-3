# Description
Test self-modification statements using CyJSAssembler.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.statements import *
indra.assemblers.cyjs import CyJSAssembler

def test_selfmod():
    cja = CyJSAssembler()
    cja.add_statements([st_selfmod])
    cja.make_model()
    assert len(cja._nodes) == 1
    assert len(cja._edges) == 1
    polarities = [edge['data']['polarity'] for edge in cja._edges]
    assert len(polarities) == 1

```
