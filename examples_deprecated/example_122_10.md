# Description
Test phosphorylation with enzyme and bound condition using PysbAssembler.

# Code
```
import xml.etree.ElementTree as ET
from indra.assemblers.pysb import PysbAssembler
import indra.assemblers.pysb.assembler as pa
from indra.statements import Agent, Complex, Phosphorylation, BoundCondition
from pysb import bng, WILD, Monomer, Annotation
from pysb.testing import with_model
import pytest
from indra.assemblers.pysb.export import export_cm_network

def test_pysb_assembler_phos2():
    hras = Agent('HRAS')
    enz = Agent('BRAF', bound_conditions=[BoundCondition(hras, True)])
    sub = Agent('MEK1')
    stmt = Phosphorylation(enz, sub, 'serine', '222')
    pa = PysbAssembler([stmt])
    model = pa.make_model()
    assert len(model.rules) == 1

```
