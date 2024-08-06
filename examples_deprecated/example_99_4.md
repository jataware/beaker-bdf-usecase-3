# Description
Testing a complex with modification conditions for generating a model using KamiAssembler.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
import json
from builtins import dict, str
from indra.statements import *
from indra.assemblers.kami import KamiAssembler

mek_phos = Agent('MAP2K1', mods=[ModCondition('phosphorylation', None, None, True)], db_refs={'HGNC': '6840'})
mek_phos2 = Agent('MAP2K1', mods=[ModCondition('phosphorylation', 'S', '222', True)], db_refs={'HGNC': '6840'})
mek_phos3 = Agent('MAP2K1', mods=[ModCondition('phosphorylation', 'S', '222', False)], db_refs={'HGNC': '6840'})

def test_complex_mod_condition():
    meks = [mek_phos, mek_phos2, mek_phos3]
    for mek in meks:
        stmt = Complex([mek, erk])
        ka = KamiAssembler()
        ka.add_statements([stmt])
        model = ka.make_model()
        assert isinstance(model, dict)
        assert isinstance(model['graphs'], list)
        assert isinstance(model['typing'], list)
        graph_list = model['graphs']
        assert len(graph_list) == 3
        assert len(graph_list[1]['graph']['edges']) == 5
        assert len(graph_list[1]['graph']['nodes']) == 6

```
