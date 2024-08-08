# Description
Process a BioPAX OWL file using INDRA and organize the statements by source ID.

# Code
```
import os
from collections import defaultdict
from indra.sources import biopax
from indra.statements import *
import indra.sources.biopax.processor as bpc
from indra.util import unicode_strs
import pytest

model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'biopax_test.owl')

stmts_by_source_id = defaultdict(set)
for stmt in bp.statements:
    for ev in stmt.evidence:

```
