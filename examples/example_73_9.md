# Description
Test for the GAP statement using `CxAssembler` to verify the generated CX model.

# Code
```
from indra.statements import *
from indra.assemblers.cx import CxAssembler


def test_gap():
    cxa = CxAssembler()
    cxa.add_statements([st_gap])
    cxa.make_model()
    assert len(cxa.cx['nodes']) == 2

```
