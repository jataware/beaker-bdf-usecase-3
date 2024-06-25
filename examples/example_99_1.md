# Description
Testing a complex with no conditions for generating a model using KamiAssembler.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
import json
from builtins import dict, str
from indra.statements import *
from indra.assemblers.kami import KamiAssembler

mek = Agent('MAP2K1', db_refs={'HGNC': '6840'})

def test_complex_no_conditions():
    stmt = Complex([mek, erk])
    ka = KamiAssembler()
    ka.add_statements([stmt])
    model = ka.make_model()
    assert isinstance(model, dict)
    assert isinstance(model['graphs'], list)
    assert isinstance(model['typing'], list)
    graph_list = model['graphs']
    assert len(graph_list) == 3
    assert len(graph_list[1]['graph']['edges']) == 4
    assert len(graph_list[1]['graph']['nodes']) == 5

```
