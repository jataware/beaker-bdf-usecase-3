# Description
Testing filtering of grounded statements by score threshold.

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

def test_filter_grounded_only_score():
    route = 'preassembly/filter_grounded_only'
    c1 = Event(Concept('x', db_refs={'a': [('x', 0.5), ('y', 0.8)]}))
    c2 = Event(Concept('x', db_refs={'a': [('x', 0.7), ('y', 0.9)]}))
    st1 = Influence(c1, c2)
    st_out = _post_stmts_preassembly([st1], route)
    assert len(st_out) == 1
    st_out = _post_stmts_preassembly([st1], route, score_threshold=0.4)
    assert len(st_out) == 1
    st_out = _post_stmts_preassembly([st1], route, score_threshold=0.6)
    assert len(st_out) == 1
    st_out = _post_stmts_preassembly([st1], route, score_threshold=0.85)
    assert len(st_out) == 0
    st_out = _post_stmts_preassembly([st1], route, score_threshold=0.95)

```
