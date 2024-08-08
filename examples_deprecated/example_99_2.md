# Description
Testing a complex with a bound condition for generating a model using KamiAssembler.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
import json
from builtins import dict, str
from indra.statements import *
from indra.assemblers.kami import KamiAssembler

braf = Agent('BRAF', db_refs={'HGNC': '1097'})
mek_braf = Agent('MAP2K1', bound_conditions=[BoundCondition(braf, True)], db_refs={'HGNC': '6840'})

def test_complex_bound_condition():
    stmt = Complex([mek_braf, erk])
    ka = KamiAssembler()
    ka.add_statements([stmt])
    model = ka.make_model()
    assert isinstance(model, dict)
    assert isinstance(model['graphs'], list)
    assert isinstance(model['typing'], list)
    graph_list = model['graphs']
    assert len(graph_list) == 3
    assert len(graph_list[1]['graph']['edges']) == 6
    assert len(graph_list[1]['graph']['nodes']) == 7

```
