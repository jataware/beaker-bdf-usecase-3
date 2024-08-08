# Description
Test print CyJS graph using CyJSAssembler.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from indra.statements import *
from indra.assemblers.cyjs import CyJSAssembler
mek = Agent('MAP2K1', db_refs={'HGNC': '6840', 'TEXT': 'mek1'})
erk = Agent('MAPK1', db_refs={'UP': 'P28482'})
dusp = Agent('DUSP4')
st_act = Activation(mek, erk)

def test_print_cyjs_graph():
    cja = CyJSAssembler()
    cja.add_statements([st_act, st_act2])
    cja.make_model()
    cyjs_str = cja.print_cyjs_graph()
    # assert output is not empty

```
