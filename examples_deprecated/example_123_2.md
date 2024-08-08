# Description
Test case where only new abstracts are read, resulting in a specific status message.

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

def test_absonly():
    s = stats.copy()
    s['new_abstracts'] = 7
    s['new_final'] = 12
    status_msg = make_status_message(s)
    assert status_msg == 'Today I read 7 abstracts, ' + \

```
