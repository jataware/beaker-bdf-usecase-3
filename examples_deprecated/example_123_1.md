# Description
Test case where neither new abstracts nor new papers are read resulting in no status message.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from indra.tools.machine.machine import make_status_message

stats = {}
stats['new_abstracts'] = 0
stats['new_papers'] = 0
stats['orig_stmts'] = 10
stats['new_stmts'] = 10
stats['orig_final'] = 10

def test_noabs_nopaper():
    s = stats.copy()
    status_msg = make_status_message(s)

```
