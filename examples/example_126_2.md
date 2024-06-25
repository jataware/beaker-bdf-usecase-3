# Description
This example shows how to process multiple PMIDs using the RLIMS-P webservice and perform assertions on the combined results.

# Code
```
os
unittest

def test_ungrounded_endpoint_with_pmids():
    pmid_list = ['16403219', '22258404', '16961925', '22096607']
    stmts = []
    for pmid in pmid_list:
        rp = rlimsp.process_from_webservice(pmid, id_type='pmid')
        assert len(rp.statements) > 10, len(rp.statements)
        stmts.extend(rp.statements)
    assert len(stmts) == 394, len(stmts)

```
