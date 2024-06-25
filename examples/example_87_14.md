# Description
Example to create a graph and save it as a PDF file.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.statements import *

def test_save_pdf():
    st = [Phosphorylation(Agent('MAP2K1'), Agent('MAPK1'))]
    ga = GraphAssembler()
    ga.add_statements(st)
    ga.make_model()

```
