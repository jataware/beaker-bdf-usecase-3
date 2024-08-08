# Description
Test grouped model with block targeting node.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.statements import *

def test_grouping_block_targeting_node():
    st1 = Phosphorylation(Agent('A'), Agent('B'))
    st2 = Phosphorylation(Agent('C'), Agent('B'))
    cja = CyJSAssembler()
    cja.add_statements([st1, st2])
    cja.make_model(grouping=True)
    for node in cja._nodes:
        if node['data']['name'] == 'A':
            parent_a = node['data']['parent']
        if node['data']['name'] == 'B':
            parent_b = node['data']['parent']
            assert parent_b == ''
        if node['data']['name'] == 'C':
            parent_c = node['data']['parent']
    assert_element_properties(cja)
    assert parent_a == parent_c
    parent_a_name = [x['data']['name'] for x in cja._nodes if
                     x['data']['id']==parent_a][0]
    assert parent_a_name.startswith('Group')
    assert len(cja._edges) == 3
    virtual_edges = [x for x in cja._edges if
                     x['data']['i'] == 'Virtual']
    assert len(virtual_edges) == 2
    real_edges = [x for x in cja._edges if
                  x['data']['i'] != 'Virtual']

```
