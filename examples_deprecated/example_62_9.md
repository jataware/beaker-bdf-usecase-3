# Description
Test the Pathway Commons 'pathsfromto' web service using INDRA's BioPAX processor.

# Code
```
import pytest
from indra.sources import biopax

def test_pathsfromto():
    bp = biopax.process_pc_pathsfromto(['MAP2K1'], ['MAPK1'])
    assert_pmids(bp.statements)
    assert_source_sub_id(bp.statements)
    assert unicode_strs(bp.statements)
    num_unique = len({s.get_hash(shallow=False) for s in bp.statements})

```
