# Description
Process a CX file and verify the processor object

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
os
indra.sources.ndex_cx import process_cx_file

ncp_file = \
    process_cx_file(os.path.join(path_this, 'merged_BRCA1_formatted.cx'))


def test_process_cx_file():

```
