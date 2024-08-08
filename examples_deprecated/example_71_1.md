# Description
Example of using CTDChemicalGeneProcessor to get statement types based on a provided pattern.

# Code
```
import os
from indra.statements import *
from indra.sources.ctd.processor import CTDChemicalGeneProcessor


def test_statement_type_mapping():
    st = CTDChemicalGeneProcessor.get_statement_types(
        'decreases^phosphorylation', 'X',
        'X decreases the phosphorylation of Y')
    assert set(st.values()) == {Dephosphorylation}, st

    st = CTDChemicalGeneProcessor.get_statement_types(
        'decreases^reaction|increases^phosphorylation', 'X',
        'X decreases the reaction [Z increases the phosphorylation of Y]')

```
