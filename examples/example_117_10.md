# Description
Combining modification statements without enzymes present.

# Code
```
import os
import unittest
from indra.preassembler import Preassembler
from indra.statements import *

def test_modification_refinement_residue_noenz():
    erbb3 = Agent('Erbb3')
    st1 = Phosphorylation(None, erbb3)
    st2 = Phosphorylation(None, erbb3, 'Y')
    pa = Preassembler(bio_ontology, stmts=[st1, st2])
    pa.combine_related()

```
