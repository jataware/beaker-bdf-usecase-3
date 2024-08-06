# Description
Initialize a TsvAssembler with statements and generate a TSV model.

# Code
```
import os
from indra.sources import signor
from indra.assemblers.tsv import TsvAssembler

from .test_signor import test_data_file, test_complexes_file
sp = signor.process_from_file(test_data_file, test_complexes_file, delimiter=';')

def test_tsv_init():
    ta = TsvAssembler(stmts)

```
