# Description
Test the extract_statements method to verify retrieved statements from the ACSN processor.

# Code
```
import requests
from indra.sources.acsn import api
from indra.sources.acsn.processor import AcsnProcessor

relations_df = pandas.read_csv(api.ACSN_RELATIONS_URL, sep='\t')
gmt_file = requests.get(api.ACSN_CORRESPONDENCE_URL).text.split('\n')
correspondence_dict = api._transform_gmt(gmt_file)

def test_extract_statements():
    ap.extract_statements()
    stmts = ap.statements
    assert stmts[345].evidence[0].source_api == 'acsn'
    test_stmt = [stmt for stmt in stmts if(any(ag.name == 'SIVA1'
                                               for ag in stmt.agent_list()) and
                                           any(ag.name == 'TRAF2'
                                               for ag in stmt.agent_list()))]
    assert test_stmt[0] in stmts

```
