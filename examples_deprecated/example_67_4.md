# Description
This code example demonstrates how to use the `get_drug_inhibition_stmts` function from the `chembl_client` module to retrieve drug inhibition statements for VEMURAFENIB and verify the returned statements.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from indra.statements import Agent
from indra.databases import chembl_client
from indra.util import unicode_strs
import pytest


@pytest.mark.webservice
@pytest.mark.slow
@pytest.mark.nogha
def test_get_drug_inhibition_stmts_vem():
    stmts = chembl_client.get_drug_inhibition_stmts(vem)
    assert len(stmts) > 0
    for st in stmts:
        assert unicode_strs(st)
        assert len(st.evidence) >= 1
        for ev in st.evidence:
            assert ev.pmid
            assert ev.annotations
            assert ev.source_api == 'chembl'

```
