# Description
Query post-translational modifications (PTMs) from the OmniPath web API and process the results to create statements.

# Code
```
import requests
from indra.sources.omnipath import OmniPathProcessor
from indra.sources.omnipath.api import op_url
from indra.statements import Agent
from indra.ontology.standardize import standardize_agent_name

JAK2_UPID = 'O60674'
JAK2_AG = Agent(None, db_refs={'UP': JAK2_UPID})

def test_mods_from_web():
    params = {'format': 'json', 'substrates': JAK2_UPID,
              'fields': ['sources', 'references']}
    ptm_url = '%s/ptms' % op_url
    res = requests.get(ptm_url, params=params)
    assert res.status_code == 200
    assert res.text
    ptm_json = res.json()
    assert ptm_json[0]['substrate'] == JAK2_UPID, ptm_json[0]['substrate']
    op = OmniPathProcessor(ptm_json=ptm_json)
    op.process_ptm_mods()
    stmts = op.statements
    assert JAK2_AG.name in [a.name for a in stmts[0].agent_list()],\
        stmts[0].agent_list()
    assert 'omnipath' == stmts[0].evidence[0].source_api,\

```
