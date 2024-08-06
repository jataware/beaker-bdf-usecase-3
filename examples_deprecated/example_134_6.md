# Description
Example of how to validate statements using INDRA's validation functions, demonstrating handling of unknown namespaces and invalid agent scenarios.

# Code
```
import pytest
from indra.statements.validate import *

def test_statement_validate():
    stmt = Phosphorylation(None, Agent('ERK', db_refs={'FPLX': 'ERK'}))
    assert validate_statement(stmt)
    assert_valid_statement(stmt)
    stmt = Phosphorylation(None, Agent('ERK', db_refs={'XXX': 'ERK'}))
    with pytest.raises(UnknownNamespace):
        assert_valid_statement(stmt)
    assert not validate_statement(stmt)

    assert not validate_statement(Phosphorylation(None, None))
    assert not validate_statement(Phosphorylation(Agent('x'), None))
    assert not validate_statement(Inhibition(None, None))
    assert not validate_statement(Inhibition(None, Agent('x')))
    assert not validate_statement(Gef(Agent('x'), None))
    assert not validate_statement(Complex([None, Agent('x')]))

```
