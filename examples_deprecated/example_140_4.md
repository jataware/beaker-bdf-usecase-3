# Description
Generate a TSV model from a TsvAssembler containing statements, and confirm the file was created.

# Code
```
import os
from indra.sources import signor
from indra.assemblers.tsv import TsvAssembler

from .test_signor import test_data_file, test_complexes_file
sp = signor.process_from_file(test_data_file, test_complexes_file, delimiter=';')

def test_make_model():
    ta = TsvAssembler(stmts)
    ta.make_model('tsv_test.tsv')

```
