# Description
Test grouped model with block targeting block.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.statements import *

def test_grouping_block_targeting_block():
    st1 = Phosphorylation(Agent('A'), Agent('B'))
    st2 = Phosphorylation(Agent('A'), Agent('C'))
    st3 = Phosphorylation(Agent('D'), Agent('B'))
    st4 = Phosphorylation(Agent('D'), Agent('C'))
    cja = CyJSAssembler()
    cja.add_statements([st1, st2, st3, st4])
    cja.make_model(grouping=True)
    for node in cja._nodes:
        if node['data']['name'] == 'A':
            parent_a = node['data']['parent']
        if node['data']['name'] == 'B':
            parent_b = node['data']['parent']
        if node['data']['name'] == 'C':
            parent_c = node['data']['parent']
        if node['data']['name'] == 'D':
            parent_d = node['data']['parent']
    assert_element_properties(cja)
    assert parent_b == parent_c
    assert parent_a == parent_d
    parent_b_name = [x['data']['name'] for x in cja._nodes if
                     x['data']['id']==parent_b][0]
    parent_a_name = [x['data']['name'] for x in cja._nodes if
                     x['data']['id']==parent_a][0]
    assert parent_b_name.startswith('Group')
    assert parent_a_name.startswith('Group')
    assert len(cja._edges) == 5
    virtual_edges = [x for x in cja._edges if
                     x['data']['i'] == 'Virtual']
    assert len(virtual_edges) == 4
    real_edges = [x for x in cja._edges if
                  x['data']['i'] != 'Virtual']

```
