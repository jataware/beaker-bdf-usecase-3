# Description
Test for the GEF statement using `CxAssembler` to verify the generated CX model.

# Code
```
from indra.statements import *
from indra.assemblers.cx import CxAssembler


def test_gef():
    cxa = CxAssembler()
    cxa.add_statements([st_gef])
    cxa.make_model()
    assert len(cxa.cx['nodes']) == 2

```
