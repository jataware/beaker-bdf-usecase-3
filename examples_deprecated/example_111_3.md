# Description
Fetch ligand-receptor interactions from the OmniPath web API and process the results to create statements.

# Code
```
import requests
from indra.sources.omnipath import OmniPathProcessor
from indra.sources.omnipath.api import op_url
from indra.statements import Agent
from indra.ontology.standardize import standardize_agent_name

CALM1_UPID = 'P0DP23'
CALM1_AG = Agent(None, db_refs={'UP': CALM1_UPID})

def test_ligrec_from_web():
    params = {'format': 'json', 'datasets': ['ligrecextra'],
              'fields': ['curation_effort', 'entity_type', 'references',
                         'resources', 'sources', 'type'],
              'sources': [CALM1_UPID]}
    query_url = '%s/interactions' % op_url
    res = requests.get(query_url, params)
    assert res.status_code == 200
    assert res.text
    assert 'error' not in res.text.lower()
    ligrec_json = res.json()
    assert ligrec_json[0]['source'] == CALM1_UPID
    op = OmniPathProcessor(ligrec_json=ligrec_json)
    op.process_ligrec_interactions()
    stmts = op.statements
    assert CALM1_AG.name in [a.name for a in stmts[0].agent_list()], \
        stmts[0].agent_list()
    assert 'omnipath' == stmts[0].evidence[0].source_api,\

```
