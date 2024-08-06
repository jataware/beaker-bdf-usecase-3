# Description
Process data from Signor and create statements using the signor module.

# Code
```
import os
from indra.sources import signor

from .test_signor import test_data_file, test_complexes_file
sp = signor.process_from_file(test_data_file, test_complexes_file,
                              delimiter=';')

```
