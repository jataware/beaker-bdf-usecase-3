# Description
Add statements to an existing TsvAssembler instance and verify the statements were added.

# Code
```
import os
from indra.sources import signor
from indra.assemblers.tsv import TsvAssembler

from .test_signor import test_data_file, test_complexes_file
sp = signor.process_from_file(test_data_file, test_complexes_file, delimiter=';')

def test_tsv_add_stmts():
    ta = TsvAssembler()
    ta.add_statements(stmts)

```
