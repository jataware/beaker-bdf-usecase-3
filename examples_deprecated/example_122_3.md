# Description
Test complex formation with a bound condition using PysbAssembler.

# Code
```
import xml.etree.ElementTree as ET
from indra.assemblers.pysb import PysbAssembler
import indra.assemblers.pysb.assembler as pa
from indra.statements import Agent, Complex, BoundCondition
from pysb import bng, WILD, Monomer, Annotation
from pysb.testing import with_model
import pytest
from indra.assemblers.pysb.export import export_cm_network

def test_pysb_assembler_complex3():
    hras = Agent('HRAS')
    member1 = Agent('BRAF', bound_conditions=[BoundCondition(hras, True)])
    member2 = Agent('MEK1')
    stmt = Complex([member1, member2])
    pa = PysbAssembler([stmt])
    model = pa.make_model()
    assert len(model.rules) == 2

```
