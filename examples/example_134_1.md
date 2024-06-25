# Description
Example of how to validate database references (db_refs) and namespaces (ns) using INDRA's validation functions, including handling unknown identifiers.

# Code
```
import pytest

def test_db_refs_validate():
    assert validate_db_refs({'HGNC': '1234'})
    assert not validate_db_refs({'XXX': '1234'})
    assert not validate_db_refs({'HGNC': 'ABCD1'})

    assert validate_ns('UP')
    assert not validate_ns('XXX')
    assert validate_id('MESH', 'D123456')
    assert not validate_id('CHEBI', '12345')

    assert_valid_id('NXPFA', '1234')
    assert_valid_id('TEXT', 'hello')
    with pytest.raises(UnknownIdentifier):

```
