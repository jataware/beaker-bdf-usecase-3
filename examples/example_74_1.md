# Description
Test activation statements using CyJSAssembler.

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

def test_act():
    cja = CyJSAssembler()
    cja.add_statements([st_act, st_act2])
    cja.make_model()
    assert len(cja._nodes) == 3
    assert len(cja._edges) == 2
    polarities = [edge['data']['polarity'] for edge in cja._edges]
    assert len(set(polarities))==2
    assert 'positive' in polarities
    assert 'negative' in polarities
    db_refs = [node['data']['db_refs'] for node in cja._nodes]
    for node, refs in zip(cja._nodes, db_refs):
        if node['data']['name'] == 'MAP2K1':
            assert refs.get('HGNC') == \
                'https://identifiers.org/hgnc:6840', refs
            assert refs.get('TEXT') == 'mek1', refs
        if node['data']['name'] == 'MAPK1':
            assert refs.get('UniProt')
        if node['data']['name'] == 'DUSP4':

```
