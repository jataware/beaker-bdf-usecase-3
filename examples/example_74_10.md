# Description
Test grouped model with node targeting and block targeting node.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.statements import *

def test_grouping_node_targeting_block_targeting_node():
    st1 = Phosphorylation(Agent('A'), Agent('B'))
    st2 = Phosphorylation(Agent('A'), Agent('C'))
    st3 = Phosphorylation(Agent('B'), Agent('D'))
    st4 = Phosphorylation(Agent('C'), Agent('D'))
    cja = CyJSAssembler()
    cja.add_statements([st1, st2, st3, st4])
    cja.make_model(grouping=True)
    for node in cja._nodes:
        if node['data']['name'] == 'A':
            parent_a = node['data']['parent']
            assert parent_a == ''
        if node['data']['name'] == 'B':
            parent_b = node['data']['parent']
        if node['data']['name'] == 'C':
            parent_c = node['data']['parent']
        if node['data']['name'] == 'D':
            parent_d = node['data']['parent']
            assert parent_d == ''
    assert_element_properties(cja)
    assert parent_b == parent_c
    parent_b_name = [x['data']['name'] for x in cja._nodes if
                     x['data']['id']==parent_b][0]
    assert parent_b_name.startswith('Group')
    assert len(cja._edges) == 6
    virtual_edges = [x for x in cja._edges if
                     x['data']['i'] == 'Virtual']
    assert len(virtual_edges) == 4
    real_edges = [x for x in cja._edges if
                  x['data']['i'] != 'Virtual']

```
