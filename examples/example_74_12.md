# Description
Test edge aggregation between non-grouped nodes.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from indra.statements import *
from indra.assemblers.cyjs import CyJSAssembler
mek = Agent('MAP2K1', db_refs={'HGNC': '6840', 'TEXT': 'mek1'})
erk = Agent('MAPK1', db_refs={'UP': 'P28482'})
st_phos_Y = Phosphorylation(mek, erk, residue='Y')

def test_edge_aggregation_between_nongroup_nodes():
    cja = CyJSAssembler()
    cja.add_statements([st_phos_Y, st_phos_T])
    cja.make_model(grouping=False)
    assert len(cja._nodes) == 2
    assert len(cja._edges) == 1
    for edge in cja._edges:
        assert len(edge['data']['uuid_list']) == 2
    for node in cja._nodes:
        assert len(node['data']['uuid_list']) == 2
    cja = CyJSAssembler()
    cja.add_statements([st_phos_Y, st_phos_T])
    cja.make_model(grouping=True)
    assert len(cja._nodes) == 2
    assert len(cja._edges) == 1
    for edge in cja._edges:
        assert len(edge['data']['uuid_list']) == 2
    for node in cja._nodes:

```
