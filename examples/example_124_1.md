# Description
Demonstration of filtering grounded statements preassembly route with various conditions and options.

# Code
```
import json
from datetime import datetime
from copy import deepcopy
import pytest
from os import path
from rest_api.api import api
from indra.statements import *

HERE = path.dirname(path.abspath(__file__))

a = Agent('a', db_refs={'HGNC': '1234', 'TEXT': 'a'})
b = Agent('b', db_refs={'UP': 'P15056', 'TEXT': 'b'})
c = Agent('c', db_refs={'FplX': 'XXX', 'TEXT': 'c'})
d = Agent('d', db_refs={'TEXT': 'd'})
e = Agent('e', db_refs={'CHEBI': 'CHEBI:1234', 'TEXT': 'e'})
f = Agent('b', db_refs={'UP': 'P28028', 'TEXT': 'b'})
g = Agent('g', db_refs={'FplX': 'ERK'})
h = Agent('g', mods=[ModCondition('phosphorylation', 'S', '202')],
          mutations=[MutCondition('858', 'L', 'R')],
          activity=ActivityCondition('activity', True), location='nucleus',
          bound_conditions=[BoundCondition(a), BoundCondition(b)])
i = Agent('a', db_refs={'HGNC': '1234', 'TEXT': 'a'},
          bound_conditions=[BoundCondition(d)])
j = Agent('a', db_refs={'HGNC': '1234', 'TEXT': 'a'},
          bound_conditions=[BoundCondition(b)])
k = Agent('a', db_refs={'HGNC': '1234', 'TEXT': 'a'},
          bound_conditions=[BoundCondition(f)])
l = Agent('a', db_refs={'HGNC': '1234', 'TEXT': 'a'},
          bound_conditions=[BoundCondition(a)])

mapk1 = Agent('MAPK1', db_refs={'HGNC':'6871', 'UP':'P28482'})
erk = Agent('ERK', db_refs={'FplX': 'ERK'})
st1 = Phosphorylation(
    a, b, evidence=[Evidence(text='a->b', source_api='assertion')])
st2 = Phosphorylation(
    a, d, evidence=[Evidence(text='a->d', source_api='assertion')])
st3 = Phosphorylation(
    c, d, evidence=[Evidence(text='c->d', source_api='assertion')])
st4 = Phosphorylation(
    b, e, evidence=[Evidence(text='b->e', source_api='assertion')])
st5 = Phosphorylation(
    None, b, evidence=[Evidence(text='->b', source_api='assertion')])
st6 = Phosphorylation(
    None, d, evidence=[Evidence(text='->d', source_api='assertion')])
st7 = Phosphorylation(
    None, e, evidence=[Evidence(text='->e', source_api='assertion')])
st8 = Phosphorylation(
    b, f, evidence=[Evidence(text='b->f', source_api='assertion')])
st9 = Phosphorylation(
    None, f, evidence=[Evidence(text='->f', source_api='assertion')])
st10 = Phosphorylation(
    None, g, evidence=[Evidence(text='->g', source_api='assertion')])
st11 = Phosphorylation(
    None, h, evidence=[Evidence(text='->h', source_api='assertion')])
st12 = Phosphorylation(
    a, b, evidence=[Evidence(epistemics={'direct': True})])
st13 = Phosphorylation(
    a, b, evidence=[Evidence(epistemics={'direct': False})])
st14 = Activation(a, b, 'activity')
st15 = Activation(a, b, 'kinase')
st14.supports = [st15]
st15.supported_by = [st14]
st16 = Phosphorylation(a, mapk1)
st17 = Phosphorylation(a, erk)
st18 = Phosphorylation(a, i)
st19 = Phosphorylation(a, j)
st20 = Phosphorylation(a, k)
st21 = Phosphorylation(a, l)
st1.belief = 0.9
st2.belief = 0.8
st3.belief = 0.7

def _call_api(method, route, *args, **kwargs):
    tc = api.app.test_client()
    req_meth = getattr(tc, method)
    start = datetime.now()
    print("Submitting request to '%s' at %s." % ('/' + route, start))
    print("\targs:", args)
    print("\tkwargs:", kwargs)
    res = req_meth(route, *args, **kwargs)
    end = datetime.now()
    print("Got result with %s at %s after %s seconds."
          % (res.status_code, end, (end-start).total_seconds()))
    assert res.status_code == 200, res.status_code
    return res

def _post_stmts_preassembly(stmts, route, **kwargs):
    stmts_json = stmts_to_json(stmts)
    req_json = {'statements': stmts_json}
    if kwargs:
        req_json.update(kwargs)
    res = _call_api('post', route, json=req_json)
    res_json = json.loads(res.get_data())
    assert 'statements' in res_json
    st_out = stmts_from_json(res_json.get('statements'))

def test_filter_grounded_only():
    route = 'preassembly/filter_grounded_only'
    st_out = _post_stmts_preassembly([st1, st4], route)
    assert len(st_out) == 2
    st_out = _post_stmts_preassembly([st3], route)
    assert len(st_out) == 0

    # Do we filter out a statement with an ungrounded bound condition?
    st_out = _post_stmts_preassembly([st18], route)
    assert len(st_out) == 0

    # When we request to remove ungrounded bound conditions, do we?
    st18_copy = deepcopy(st18)
    assert len(st18_copy.sub.bound_conditions) == 1
    st_out = _post_stmts_preassembly([st18_copy], route, remove_bound=True)
    assert len(st_out[0].sub.bound_conditions) == 0

    # When we request to remove ungrounded bound conditions, do we leave
    # grounded bound conditions in place?
    st19_copy = deepcopy(st19)
    assert len(st19_copy.sub.bound_conditions) == 1
    st_out = _post_stmts_preassembly([st19_copy], route, remove_bound=True)
    assert len(st_out[0].sub.bound_conditions) == 1

    # Do we filter out a statement with an grounded bound condition?
    st_out = _post_stmts_preassembly([st19], route)

```
