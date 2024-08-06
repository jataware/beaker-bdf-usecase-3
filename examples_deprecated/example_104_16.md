# Description
Test for detecting duplicate SVOs within the same sentence using `process_file` method.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
os.path import join, dirname
indra.sources.medscan.api import process_file

def test_handle_duplicates():
    # Does the processor detect duplicate SVOs within the same sentence?
    fname = os.path.join(data_folder, 'test_duplicate_SVO.csxml')
    mp = process_file(fname, None)

    statements = mp.statements

```
