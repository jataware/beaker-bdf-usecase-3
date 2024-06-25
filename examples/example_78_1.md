# Description
Process a DrugBank XML file and perform assertions on the data to validate the processing.

# Code
```
import os
from indra.sources import drugbank


def test_drugbank_sample():
    dp = drugbank.process_xml(test_file)
    assert len(dp.statements) == 1
    stmt = dp.statements[0]
    assert len(stmt.evidence) == 6
    assert all(ev.pmid for ev in stmt.evidence)
    assert all(ev.source_api == 'drugbank' for ev in stmt.evidence)
    drug = stmt.subj
    assert drug.name == 'lepirudin'
    assert drug.db_refs['DRUGBANK'] == 'DB00001'
    assert drug.db_refs['CAS'] == '138068-37-8'

    target = stmt.obj
    assert target.name == 'F2'
    assert target.db_refs['HGNC'] == '3535'
    assert target.db_refs['UP'] == 'P00734'

```
