# Description
Test for hub layout using `CxAssembler` and `hub_layout` from `indra.assemblers.cx`.

# Code
```
from indra.statements import *
from indra.assemblers.cx import CxAssembler, hub_layout

mek = Agent('MAP2K1', db_refs={'HGNC': '6840'})
erk = Agent('MAPK1', db_refs={'UP': 'P28482'})
dusp = Agent('DUSP4')
st_phos = Phosphorylation(mek, erk)
st_dephos = Dephosphorylation(dusp, erk)

def test_hub_layout():
    stmts = [st_phos, st_dephos, st_act]
    cxa = CxAssembler(stmts)
    cxa.make_model()
    graph = hub_layout.cx_to_networkx(cxa.cx)
    erk = hub_layout.get_node_by_name(graph, 'MAPK1')
    hub_layout.add_semantic_hub_layout(cxa.cx, 'MAPK1')
    assert cxa.cx['cartesianLayout']
    for node in cxa.cx['cartesianLayout']:
        if node['node'] == erk:
            assert node['x'] == 0.0
            assert node['y'] == 0.0
        else:
            assert node['x'] != 0
            assert node['y'] != 0

    node_classes = hub_layout.classify_nodes(graph, erk)
    assert node_classes[hub_layout.get_node_by_name(graph, 'DUSP4')] == \
        (1, 'modification', 'other')
    assert node_classes[hub_layout.get_node_by_name(graph, 'MAP2K1')] in \

```
